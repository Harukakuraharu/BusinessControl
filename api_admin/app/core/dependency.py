<<<<<<< HEAD
from typing import Annotated, AsyncIterator
=======
from typing import Annotated
>>>>>>> 3f2822f (Complete servis with admin and company)

import jwt
import sqlalchemy as sa
from database import models
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.settings import config
<<<<<<< HEAD


async def get_session() -> AsyncIterator[AsyncSession]:
    """Get session for execution of the request"""
    async with AsyncSession(
        create_async_engine(config.async_dsn)
    ) as session:  # type: ignore[arg-type]
=======
from schemas import schemas


async def get_session():
    async with AsyncSession(create_async_engine(config.async_dsn)) as session:
>>>>>>> 3f2822f (Complete servis with admin and company)
        yield session


AsyncSessionDependency = Annotated[
    AsyncSession, Depends(get_session, use_cache=True)
]


async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    session: AsyncSessionDependency,
<<<<<<< HEAD
) -> models.User:
    """Get current user who send request"""
=======
) -> schemas.UserResponse:
>>>>>>> 3f2822f (Complete servis with admin and company)
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


<<<<<<< HEAD
GetCurrentUserDependency = Annotated[models.User, Depends(get_current_user)]


async def check_permission(
    current_user: GetCurrentUserDependency,
) -> models.User:
    """Check permission current user who send request for create company"""
=======
GetCurrentUserDependency = Annotated[
    schemas.UserResponse, Depends(get_current_user)
]


async def check_permission(current_user: GetCurrentUserDependency):
>>>>>>> 3f2822f (Complete servis with admin and company)
    if current_user.is_admin is not True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You have not a permission to perform this action",
        )
    return current_user


<<<<<<< HEAD
AdminPermissionDependency = Annotated[models.User, Depends(check_permission)]


async def check_permission_company(
    current_user: AdminPermissionDependency,
) -> models.User:
    """Check get company for current user who send request"""
=======
AdminPermissionDependency = Annotated[
    schemas.UserResponse, Depends(check_permission)
]


async def check_permission_company(current_user: AdminPermissionDependency):
>>>>>>> 3f2822f (Complete servis with admin and company)
    if current_user.organization is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Company not found")
    return current_user


CompanyPermissionDependency = Annotated[
<<<<<<< HEAD
    models.User, Depends(check_permission_company)
=======
    schemas.UserResponse, Depends(check_permission_company)
>>>>>>> 3f2822f (Complete servis with admin and company)
]
