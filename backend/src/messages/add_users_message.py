from typing import List

from .abstract_message import AbstractMessage, MessageType
from ..managers.connection import Connection


class AddUsersMessage(AbstractMessage):
    async def get_message(connections: List[Connection]) -> dict:
        try:
            conns = await connections
            return {
                'message_type': MessageType.ADD_USERS,
                'users': [c.user.as_dict() for c in conns]
            }
        except Exception:
            return dict()
