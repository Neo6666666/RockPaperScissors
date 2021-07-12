from backend.src.messages.abstract_message import MessageType
from typing import Dict, List

from fastapi import WebSocket

from tortoise.query_utils import Q

from ..users.utils import GetUserByID

from .connection import Connection


from ..messages.message_factory import MessageFactory


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[Connection] = {}

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
        await websocket.accept()
        new_user = await GetUserByID({'id': user_id})
        new_connection = Connection(user=new_user, websocket=websocket)
        personal_message = await MessageFactory.create_message(
            MessageType.ADD_USERS,
            self.active_connections
        )
        to_all_messaage = await MessageFactory.create_message(
            MessageType.NEW_USER,
            new_user
        )
        await self.broadcast(message=to_all_messaage)
        await self.send_personal_message(
            message=personal_message,
            websocket=websocket)
        self.active_connections[user_id] = new_connection

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
