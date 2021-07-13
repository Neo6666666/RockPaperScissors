from abc import ABC, abstractmethod
from enum import Enum


class MessageType(Enum):
    NEW_USER = 'NEW_USER'
    ADD_USERS = 'ADD_USERS'


class AbstractMessage(ABC):
    @staticmethod
    @abstractmethod
    async def get_message(*args, **kwargs) -> dict:
        raise NotImplementedError
