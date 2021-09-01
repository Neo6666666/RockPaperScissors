from abc import ABC, abstractmethod
from enum import Enum


class MessageType(str, Enum):
    NEW_USER = 'NEW_USER'
    ADD_USERS = 'ADD_USERS'
    REMOVE_USER = 'RM_USER'


class AbstractMessage(ABC):
    @staticmethod
    @abstractmethod
    async def get_message(*args, **kwargs) -> dict:
        raise NotImplementedError
