from abc import ABC, abstractmethod
from enum import Enum


class MessageType(Enum):
    NEW_USER = 'NEW_USER'
    ADD_USERS = 'ADD_USERS'


class AbstractMessage(ABC):
    @abstractmethod
    async def get_message(self, *args, **kwargs) -> dict:
        raise NotImplementedError
