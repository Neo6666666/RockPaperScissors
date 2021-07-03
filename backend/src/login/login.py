import logging

from fastapi import APIRouter

from tortoise.contrib.fastapi import HTTPNotFoundError

from ..users.models import User_Pydantic, UserIn_Pydantic, Users


logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/login', response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def login(user: UserIn_Pydantic):
    # logger.warning(f'{username} - {password}')
    return await User_Pydantic.from_queryset_single(Users.get(**user.dict(exclude_unset=True)))