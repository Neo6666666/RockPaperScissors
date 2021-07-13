from typing import Dict, List

from fastapi import WebSocket

from tortoise.query_utils import Q

from ..users.utils import GetUserByID

from .connection import Connection


from ..messages.new_user_message import NewUserMessage
from ..messages.add_users_message import AddUsersMessage


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
        new_user = await GetUserByID(user_id)
        new_connection = Connection(user=new_user, websocket=websocket)
        personal_message = await AddUsersMessage.get_message(
            connections=self.active_connections)
        to_all_messaage = await NewUserMessage.get_message(new_user)
        await self.broadcast(message=to_all_messaage)
        await self.send_personal_message(
            message=personal_message,
            websocket=new_connection.websocket)
        self.active_connections[user_id] = new_connection

    def disconnect(self, websocket: WebSocket):
        """
            broadcast message to all users exept deleted one(MessageType.REMOVE_USER)
            remove connection from active_connections
        """
        for k, v in self.active_connections.items():
            if websocket is v.websocket:
                self.active_connections.pop(k)

    async def send_personal_message(self, message, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.websocket.send_json(message)


manager = ConnectionManager()


async def get_manager() -> ConnectionManager:
    return manager
