from typing import Dict, List, Tuple, Union

from ..users.utils import GetUserByID

from ..game.models import Invite


Answer = Tuple[Dict[str, Union[str, List[str]]], Dict[str, Union[str, int]]]


async def invite_user_handler(data: dict) -> Answer:
    """
     { 'content_type': 'INVITE_USER', 'host_id': int, 'guest_id': int }
                                    ||
                                    \/
     { 'content_type': 'ROOM_AWAIT', 'host_username': str, 'room_id': str, }
    """

    host = await GetUserByID(data.get('host_id'))
    guest = await GetUserByID(data.get('guest_id'))
    invite = await Invite.create(**{'creator': host, 'guest': guest})
    return (
        {
            'send_to': [str(guest.id), ]
        },
        {
            'content_type': 'ROOM_AWAIT',
            'host_username': host.username,
            'room_id': str(invite.uuid),
        }
    )


async def start_game(data: dict) -> Answer:
    pass


async def reject_game(data: dict) -> Answer:
    """
        {'content_type': 'CLOSE_ROOM', 'room_id': str,  }
                            ||
                            \/
        {'content_type': 'ROOM_CLOSED', 'room_id': str,  }
    """
    uuid = data.get('room_id')
    invite = await Invite.get({'uuid': uuid})
    invite.is_closed = True
    await invite.save()
    return tuple(
        {
            'send_to': [str(invite.creator.id), str(invite.guest.id)]
        },
        {
            'content_type': 'ROOM_CLOSED',
            'room_id': uuid,
        }
    )
