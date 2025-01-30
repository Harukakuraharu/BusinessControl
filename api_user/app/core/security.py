from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi import HTTPException, status

from core.dependency import AsyncSessionDependency
from core.settings import config
from crud.user_crud import UserCrud
from tests_config import utils



async def auth(session: AsyncSessionDependency, email: str, password: str):
    user = await UserCrud(session).get_user(email)
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User is not exists")
    if not user or not utils.check_password(password, user.password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, "Incorrect password or username"
        )
    return user


