from fastapi import APIRouter

from tortoise.contrib.fastapi import HTTPNotFoundError

from ..users.models import User_Pydantic, UserIn_Pydantic
from ..users.utils import GetUser, SetUserIsActive


router = APIRouter()


@router.post('/login', response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def login(user: UserIn_Pydantic):
    user = await GetUser(**user.dict(exclude_unset=True))
    await SetUserIsActive(user)
    return await User_Pydantic.from_queryset_single(user)
