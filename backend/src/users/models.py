from enum import Enum
from typing import Any

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.pydantic.base import PydanticModel

from ..login.utils import hash_password


class Status(str, Enum):
    ACTIVE = 'Active'
    IN_GAME = 'In Game'
    OFFLINE = 'Offline'


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.BinaryField()
    salt = fields.BinaryField()
    status = fields.CharEnumField(Status, default=Status.ACTIVE)

    @classmethod
    async def create(cls: Any, **kwargs: Any) -> Any:
        salt, pw = hash_password(kwargs['password'])
        return await super().create(**kwargs, salt=salt, password_hash=pw)

    class PydanticMeta:
        exclude = ["password_hash", "salt"]

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'status': self.status,
        }


User_Pydantic = pydantic_model_creator(Users, name="User")


class UserIn_Pydantic(PydanticModel):
    username: str
    password: str
