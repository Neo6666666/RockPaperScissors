from enum import Enum

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Status(str, Enum):
    ACTIVE = 'Active'
    IN_GAME = 'In Game'
    OFFLINE = 'Offline'


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(max_length=128)
    status = fields.CharEnumField(Status, default=Status.ACTIVE)

    # class PydanticMeta:
    #     exclude = ["password_hash"]


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True)
