from typing import Dict
from .abstract_message import AbstractMessage, MessageType
from ..managers.connection import Connection


class AddUsersMessage(AbstractMessage):
    async def get_message(connections: Dict[str, Connection]) -> dict:
        try:
            # conns = await connections
            return {
                'content_type': MessageType.ADD_USERS,
                'users': [c.user.as_dict() for c in connections.values()]
            }
        except Exception:
            return dict()
