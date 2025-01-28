<<<<<<< HEAD
from core import dependency
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
from services.user_services import UserService
=======
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

>>>>>>> 09b7086 (Add user routers)

user_routers = APIRouter(
    prefix="/user",
    tags=["User"],
)


<<<<<<< HEAD
@user_routers.post("/registration/", response_model=schemas.UserResponse)
async def create_user(
    session: dependency.AsyncSessionDependency, data: schemas.UserCreate
=======
@user_routers.post("/registration/")
async def create_user(
    session: dependency.AsyncSessionDependency, data: UserCreate
>>>>>>> 09b7086 (Add user routers)
):
    """Registration of all user"""
    return await UserService(session).create_user(data)


<<<<<<< HEAD
@user_routers.post("/auth/", response_model=schemas.Token)
async def login(
    session: dependency.AsyncSessionDependency, data: schemas.UserLogin
):
=======
@user_routers.post("/auth/", response_model=Token)
async def login(session: dependency.AsyncSessionDependency, data: UserLogin):
>>>>>>> 09b7086 (Add user routers)
    """Auth user"""
    return await UserService(session).login(data)


<<<<<<< HEAD
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
=======
@user_routers.get("/me/", response_model=UserResponse)
>>>>>>> 09b7086 (Add user routers)
async def get_users_me(
    current_user: dependency.GetCurrentUserDependency,
):
    """Get info about current user"""
<<<<<<< HEAD
    user = current_user
    return user


@user_routers.patch("/me/", response_model=schemas.UserResponse)
async def update_user(
    session: dependency.AsyncSessionDependency,
    data: schemas.UserUpdate,
=======
    return current_user


@user_routers.patch("/me/", response_model=UserResponse)
async def update_user(
    session: dependency.AsyncSessionDependency,
    data: UserUpdate,
>>>>>>> 09b7086 (Add user routers)
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
