from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.core import dependency
from app.services.user_services import UserService

from schemas.users import (
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
    UserUpdate,
)


user_routers = APIRouter(
    prefix="/user",
    tags=["User"],
)


@user_routers.post("/registration/")
async def create_user(
    session: dependency.AsyncSessionDependency, data: UserCreate
):
    """Registration of all user"""
    return await UserService(session).create_user(data)


@user_routers.post("/auth/", response_model=Token)
async def login(session: dependency.AsyncSessionDependency, data: UserLogin):
    """Auth user"""
    return await UserService(session).login(data)


@user_routers.get("/me/", response_model=UserResponse)
async def get_users_me(
    current_user: dependency.GetCurrentUserDependency,
):
    """Get info about current user"""
    return current_user


@user_routers.patch("/me/", response_model=UserResponse)
async def update_user(
    session: dependency.AsyncSessionDependency,
    data: UserUpdate,
    current_user: dependency.GetCurrentUserDependency,
):
    """Update info about youself"""
    return await UserService(session).update_user(data, current_user)


@user_routers.delete("/me/", response_class=JSONResponse)
async def delete_user(
    session: dependency.AsyncSessionDependency,
    current_user: dependency.GetCurrentUserDependency,
):
    """Delete user"""
    await UserService(session).delete_user(current_user)
    return JSONResponse(
        content="Successfully deleted", status_code=status.HTTP_200_OK
    )
