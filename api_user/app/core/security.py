import bcrypt
import jwt
from core.dependency import AsyncSessionDependency
from core.settings import config
from crud.user_crud import UserCrud
from fastapi import HTTPException, status
from tests_config import utils


async def auth(session: AsyncSessionDependency, email: str, password: str):
    """Auth user with password and email"""
    user = await UserCrud(session).get_user(email)
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User is not exists")
    if not user or not utils.check_password(password, user.password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, "Incorrect password or username"
        )
    return user
