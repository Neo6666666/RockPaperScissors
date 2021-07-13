from ..users.models import Users

from .abstract_message import AbstractMessage, MessageType


class NewUserMessage(AbstractMessage):
    async def get_message(user: Users) -> dict:
        try:
            return {
                'content_type': MessageType.NEW_USER,
                'user': user.as_dict()
            }
        except Exception:
            return dict()
