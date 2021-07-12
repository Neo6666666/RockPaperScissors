from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

from .login.login import router as api_router
from .register.register_controller import router as reg_api_router
from .websockets.websocket import router as websocket_api


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/users", response_model=List[User_Pydantic])
# async def get_users():
#     return await User_Pydantic.from_queryset(Users.exclude(status=Status.OFFLINE))


app.include_router(api_router, prefix="/api")
app.include_router(reg_api_router, prefix="/api")
app.include_router(websocket_api, prefix='/users')

register_tortoise(
    app,
    db_url="sqlite://database.db",
    modules={"models": ["src.users.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
