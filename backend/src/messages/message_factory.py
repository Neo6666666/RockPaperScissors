from .abstract_message import MessageType
from .new_user_message import NewUserMessage
from .add_users_message import AddUsersMessage


class MessageFactory():
    @ staticmethod
    async def create_message(message_type: MessageType, *args) -> dict:
        if message_type == MessageType.NEW_USER:
            return await NewUserMessage.get_message(
                message_type=message_type,
                user=args[0]
            )
        elif message_type == MessageType.ADD_USER:
            return await AddUsersMessage.get_message(
                message_type=message_type,
                users=args[0]
            )
