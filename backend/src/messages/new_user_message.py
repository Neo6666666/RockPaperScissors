from backend.src.users.models import Users
from .abstract_message import AbstractMessage, MessageType


class NewUserMessage(AbstractMessage):
    async def get_message(self, *args, **kwargs) -> dict:
        try:
            mt = kwargs.pop('message_type', MessageType.NEW_USER)
            user: Users = kwargs.pop('user')
            return {
                'message_type': mt,
                'user': user.as_dict()
            }
        except Exception:
            return dict()
