from typing import Callable, Dict

from ..messages.abstract_message import MessageType

from .handlers import invite_user_handler, reject_game, start_game, make_turn


factory: Dict[str, Callable] = {
    MessageType.INVITE_USER.value: invite_user_handler,
    MessageType.CLOSE_ROOM.value: reject_game,
    MessageType.ROOM_ACCEPT.value: start_game,
    MessageType.MAKE_TURN.value: make_turn,
}
