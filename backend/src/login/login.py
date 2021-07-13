from fastapi import APIRouter, HTTPException

from tortoise.contrib.fastapi import HTTPNotFoundError

from ..users.models import User_Pydantic, UserIn_Pydantic, Users
from ..users.utils import GetUserByUsername, SetUserIsActive

from .utils import validate_password


router = APIRouter()


@router.post('/login', response_model=User_Pydantic,
             responses={404: {"model": HTTPNotFoundError}})
async def login(user: UserIn_Pydantic):
    user_db: Users = await GetUserByUsername(user.username)
    if validate_password(user_db.salt, user_db.password_hash, user.password):
        await SetUserIsActive(user_db)
        return await User_Pydantic.from_tortoise_orm(user_db)
    else:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
