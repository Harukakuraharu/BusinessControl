from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from services.user_services import UserService

from core import dependency
from schemas import schemas


user_routers = APIRouter(
    prefix="/user",
    tags=["User"],
)


@user_routers.post("/registration/", response_model=schemas.UserResponse)
async def create_user(
    session: dependency.AsyncSessionDependency, data: schemas.UserCreate
):
    """Registration of all user"""
    return await UserService(session).create_user(data)


@user_routers.post("/auth/", response_model=schemas.Token)
async def login(
    session: dependency.AsyncSessionDependency, data: schemas.UserLogin
):
    """Auth user"""
    return await UserService(session).login(data)


@user_routers.post(
    "/join_company/", response_model=schemas.JoinCompanyResponse
)
async def join_company(
    current_user: dependency.GetCurrentUserDependency,
    session: dependency.AsyncSessionDependency,
    data: schemas.JoinCompany,
):
    """Join in company with special code"""
    return await UserService(session).join_company(current_user, data)


@user_routers.get("/me/", response_model=schemas.UserResponse)
async def get_users_me(
    current_user: dependency.GetCurrentUserDependency,
):
    """Get info about current user"""
    return current_user


@user_routers.patch("/me/", response_model=schemas.UserResponse)
async def update_user(
    session: dependency.AsyncSessionDependency,
    data: schemas.UserUpdate,
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
