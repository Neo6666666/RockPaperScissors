from fastapi import WebSocket, WebSocketDisconnect
from fastapi import APIRouter, Depends

from ..managers.connection_manager import get_manager


router = APIRouter()


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket, client_id: int = 0):
    # TODO mngr.proceed_connection(websocket, client_id)
    mngr = await get_manager()
    await mngr.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_json()
            await mngr.proceed_data(data)
            # await mngr.send_personal_message({"You wrote": data, }, websocket)
            # await mngr.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        # TODO mngr.proceed_disconnect(websocket)
        await mngr.disconnect(websocket)
        # await mngr.broadcast(f"Client #{client_id} left the chat")
