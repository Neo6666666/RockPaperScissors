from enum import Enum
from uuid import uuid4

from tortoise import fields, models
from tortoise.fields.base import CASCADE, SET_NULL

import src.users.models


class Invite(models.Model):
    id = fields.IntField(pk=True)
    uuid = fields.UUIDField(default=uuid4, index=True, unique=True)
    creator: fields.ForeignKeyRelation['src.users.models.Users'] = fields.ForeignKeyField(
        'models.Users',
        null=True,
        related_name='creator',
        on_delete=SET_NULL
    )
    guest: fields.ForeignKeyRelation['src.users.models.Users'] = fields.ForeignKeyField(
        'models.Users',
        null=True,
        related_name='guest',
        on_delete=SET_NULL
    )

    turns: fields.ReverseRelation['Turn']


class Result(str, Enum):
    NOT_DECIDE = 'Not Decide'
    F_PLAYER_WIN = 'First Player Win'
    S_PLAYER_WIN = 'Second Player Win'
    DRAW = 'Draw'


class Turn(models.Model):
    id = fields.IntField(pk=True)
    uuid = fields.UUIDField(default=uuid4, index=True, unique=True)
    invite: fields.ForeignKeyRelation['Invite'] = fields.ForeignKeyField(
        'models.Invite',
        related_name='turns',
        on_delete=CASCADE
    )
    previous_turn: fields.ForeignKeyRelation['Turn'] = fields.ForeignKeyField(
        'models.Turn',
        null=True,
        related_name='next_turn',
        on_delete=SET_NULL
    )
    result = fields.CharEnumField(Result, default=Result.NOT_DECIDE)
