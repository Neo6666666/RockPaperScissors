from ..users.models import Users
from starlette.websockets import WebSocket


class Connection():
    def __init__(self, websocket: WebSocket, user: Users):
        self.websocket: WebSocket = websocket
        self.user: Users = user
