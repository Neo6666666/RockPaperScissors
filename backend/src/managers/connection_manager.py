from typing import Dict, Optional

from fastapi import WebSocket

from ..users.utils import GetUserByID, SetUserIsOffline, SetUserIsActive

from .connection import Connection

from ..handlers.handler_factory import factory

from ..messages.new_user_message import NewUserMessage
from ..messages.add_users_message import AddUsersMessage
from ..messages.remove_user_message import RemoveUserMessage


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, Connection] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        """
            accept websocket connection
        """
        await websocket.accept()
        await self.handle_first_connection(websocket, user_id)

    async def disconnect(self, websocket: WebSocket):
        await self.handle_disconnection(websocket)

    async def send_personal_message(self, message: dict,
                                    websocket: WebSocket) -> None:
        await websocket.send_json(message)

    async def broadcast(self, message: dict):
        for key, connection in self.active_connections.items():
            await connection.websocket.send_json(message)

    async def proceed_data(self, data: dict) -> None:
        message_type: str = data.pop('content_type')
        handler = factory.get(message_type)
        result = await handler(data)
        to = result[0].get('send_to', 'broadcast')
        if to != 'broadcast':
            for reciever in to:
                conn = self.active_connections.get(reciever)
                await self.send_personal_message(result[1], conn.websocket)
        else:
            await self.broadcast(result[1])

    async def handle_first_connection(self, websocket: WebSocket,
                                      user_id: int) -> None:
        """
            find user by id
            create connection object
            sort all active user exept connected <- not needed. 
                We already got all active users in connections!
            broadcast to all users about new one (MessageType.NEW_USER)
            send newcome user list of all active users 
                (MessageType.ADD_USERS) <- i.e. active_connections
            append new connection to active_connections
        """
        new_user = await GetUserByID(user_id)
        await SetUserIsActive(new_user)
        new_connection = Connection(user=new_user, websocket=websocket)
        personal_message = await AddUsersMessage.get_message(
            connections=self.active_connections)
        to_all_messaage = await NewUserMessage.get_message(new_user)

        await self.broadcast(message=to_all_messaage)
        await self.send_personal_message(
            message=personal_message,
            websocket=new_connection.websocket)
        self.active_connections[str(user_id)] = new_connection

    async def handle_disconnection(self, websocket: WebSocket) -> None:
        """
            broadcast message to all users exept deleted one(MessageType.REMOVE_USER)
            remove connection from active_connections
        """
        disconnected: Optional[Connection] = None
        for k, v in self.active_connections.items():
            if websocket is v.websocket:
                m = await RemoveUserMessage.get_message(v.user)
                await SetUserIsOffline(v.user)
                disconnected = k
                break
        self.active_connections.pop(disconnected)
        await self.broadcast(message=m)


manager = ConnectionManager()


async def get_manager() -> ConnectionManager:
    return manager
