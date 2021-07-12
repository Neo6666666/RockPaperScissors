from typing import List
import json

from fastapi import WebSocket

from tortoise.query_utils import Q

from ..users.models import Status, User_Pydantic, UserIn_Pydantic, Users

from logging import getLogger


logger = getLogger()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, user_id: int):
        """
            accept websocket connection
            find user by id
            create connection object
            sort all active user exept connected <- not needed. We already got all active users in connections!
            broadcast to all users about new one (MessageType.NEW_USER)
            send newcome user list of all active users (MessageType.ADD_USERS) <- i.e. active_connections
            append new connection to active_connections
        """
        logger.warning(f'Connect {user_id}')
        await websocket.accept()
        message = await User_Pydantic.from_queryset(Users.exclude(Q(status=Status.OFFLINE) | Q(id=user_id)))
        await self.send_personal_message(message={'users': [
            {
                "id": m.id,
                "username": m.username
            }
        for m in message]}, websocket=websocket)
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """
            broadcast message to all users exept deleted one(MessageType.REMOVE_USER)
            remove connection from active_connections
        """
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()


async def get_manager() -> ConnectionManager:
    return manager
