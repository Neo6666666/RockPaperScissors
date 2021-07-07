from typing import Dict


from .models import Status, Users


async def GetUser(data: Dict) -> Users:
    return await Users.get(data)


async def SetNewStatusToUser(user: Users, status: Status) -> None:
    user.status = status
    user.save()


async def SetUserIsActive(user: Users) -> None:
    await SetNewStatusToUser(user, Status.ACTIVE)


async def SetUserIsGame(user: Users) -> None:
    await SetNewStatusToUser(user, Status.IN_GAME)


async def SetUserIsOffline(user: Users) -> None:
    await SetNewStatusToUser(user, Status.OFFLINE)
