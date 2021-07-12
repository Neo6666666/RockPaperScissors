from .abstract_message import AbstractMessage, MessageType


class AddUsersMessage(AbstractMessage):
    async def get_message(self, *args, **kwargs) -> dict:
        try:
            mt = kwargs.pop('message_type', MessageType.ADD_USERS)
            users = [c.user.as_dict() for c in kwargs['connections']]
            return {
                'message_type': mt,
                'users': users
            }
        except Exception:
            return dict()
