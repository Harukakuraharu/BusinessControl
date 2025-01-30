from typing import Annotated

import jwt
import sqlalchemy as sa
from database import models
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.settings import config
from schemas import schemas


async def get_session():
    async with AsyncSession(create_async_engine(config.async_dsn)) as session:
        yield session


AsyncSessionDependency = Annotated[
    AsyncSession, Depends(get_session, use_cache=True)
]


async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    session: AsyncSessionDependency,
) -> schemas.UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token.credentials, config.SECRET_KEY, algorithms=[config.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except InvalidTokenError as err:
        raise credentials_exception from err
    stmt = sa.select(models.User).where(models.User.email == email)
    user = await session.scalar(stmt)
    if user is None:
        raise credentials_exception
    return user


GetCurrentUserDependency = Annotated[
    schemas.UserResponse, Depends(get_current_user)
]


class RoleChecker:
    def __init__(self, allowed_roles: list[models.UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: GetCurrentUserDependency):
        if (
            user.organization is None
            or user.organization.role.name not in self.allowed_roles
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You have not a permission to perform this action",
            )
        return user


ManagerPermissionDependency = Annotated[
    schemas.UserResponse,
    Depends(
        RoleChecker(
            [models.UserRole.MANAGER.name, models.UserRole.SUPER_MANAGER.name]
        )
    ),
]

EmployeerPermissionDependency = Annotated[
    schemas.UserResponse,
    Depends(RoleChecker([models.UserRole.EMPLOYEE])),
]
