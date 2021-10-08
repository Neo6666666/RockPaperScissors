from abc import ABC, abstractmethod
from enum import Enum


class MessageType(str, Enum):
    NEW_USER = 'NEW_USER'
    ADD_USERS = 'ADD_USERS'
    REMOVE_USER = 'RM_USER'
    INVITE_USER = 'INVITE_USER'
    ROOM_AWAIT = 'ROOM_AWAIT'
    ROOM_ACCEPT = 'ROOM_ACCEPT'
    CLOSE_ROOM = 'CLOSE_ROOM'
    ROOM_CLOSED = 'ROOM_CLOSED'


class AbstractMessage(ABC):
    @staticmethod
    @abstractmethod
    async def get_message(*args, **kwargs) -> dict:
        raise NotImplementedError
