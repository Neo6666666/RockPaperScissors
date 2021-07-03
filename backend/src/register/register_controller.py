from fastapi import APIRouter

from ..users.models import UserIn_Pydantic, User_Pydantic, Users


router = APIRouter()

@router.post('/register', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)