from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse

from starlette.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

from .users.models import Status, User_Pydantic, UserIn_Pydantic, Users

from .login.login import router as api_router
from .register.register_controller import router as reg_api_router


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        message = await User_Pydantic.from_queryset(Users.exclude(status=Status.OFFLINE))
        print(message)
        await self.send_personal_message(message=f"'users': {[m.json(indent=4) for m in message]}", websocket=websocket)
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(Users.exclude(status=Status.OFFLINE))


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


app.include_router(api_router, prefix="/api")
app.include_router(reg_api_router, prefix="/api")

register_tortoise(
    app,
    db_url="sqlite://database.db",
    modules={"models": ["src.users.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
