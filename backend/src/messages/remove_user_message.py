from typing import Dict
from .abstract_message import AbstractMessage, MessageType
from ..users.models import Users


class RemoveUserMessage(AbstractMessage):
    @staticmethod
    async def get_message(user: Users) -> dict:
        try:
            return {
                'content_type': MessageType.REMOVE_USER,
                'user': user.as_dict()
            }
        except Exception:
            return dict()
