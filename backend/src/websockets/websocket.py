from fastapi import WebSocket, WebSocketDisconnect
from fastapi import APIRouter, Depends

from ..managers.connection_manager import ConnectionManager, get_manager


router = APIRouter()


@router.websocket("{client_id}/")
async def websocket_endpoint(websocket: WebSocket, client_id: int,
                             mngr: ConnectionManager = Depends(get_manager)):
    # TODO mngr.proceed_connection(websocket, client_id)
    await mngr.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_json()
            # TODO mngr.proceed_data(data)
            await mngr.send_personal_message(f"You wrote: {data}", websocket)
            await mngr.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        # TODO mngr.proceed_disconnect(websocket)
        mngr.disconnect(websocket)
        await mngr.broadcast(f"Client #{client_id} left the chat")
