from typing import Callable, Dict

from ..messages.abstract_message import MessageType

from .handlers import invite_user_handler, reject_game


factory: Dict[str, Callable] = {
    MessageType.INVITE_USER.value: invite_user_handler,
    MessageType.CLOSE_ROOM.value: reject_game,
}
