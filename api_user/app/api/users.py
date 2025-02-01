<<<<<<< HEAD
<<<<<<< HEAD
from core import dependency
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
from services.user_services import UserService
=======
=======
from core import dependency
>>>>>>> e7f03f9 (Added docs)
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
<<<<<<< HEAD

>>>>>>> 09b7086 (Add user routers)
=======
from services.user_services import UserService
>>>>>>> e7f03f9 (Added docs)

user_routers = APIRouter(
    prefix="/user",
    tags=["User"],
)


<<<<<<< HEAD
<<<<<<< HEAD
@user_routers.post("/registration/", response_model=schemas.UserResponse)
async def create_user(
    session: dependency.AsyncSessionDependency, data: schemas.UserCreate
=======
@user_routers.post("/registration/")
async def create_user(
    session: dependency.AsyncSessionDependency, data: UserCreate
>>>>>>> 09b7086 (Add user routers)
=======
@user_routers.post("/registration/", response_model=schemas.UserResponse)
async def create_user(
    session: dependency.AsyncSessionDependency, data: schemas.UserCreate
>>>>>>> 3f2822f (Complete servis with admin and company)
):
    """Registration of all user"""
    return await UserService(session).create_user(data)


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
@user_routers.post("/auth/", response_model=schemas.Token)
async def login(
    session: dependency.AsyncSessionDependency, data: schemas.UserLogin
):
<<<<<<< HEAD
=======
@user_routers.post("/auth/", response_model=Token)
async def login(session: dependency.AsyncSessionDependency, data: UserLogin):
>>>>>>> 09b7086 (Add user routers)
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    """Auth user"""
    return await UserService(session).login(data)


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
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
<<<<<<< HEAD
=======
@user_routers.get("/me/", response_model=UserResponse)
>>>>>>> 09b7086 (Add user routers)
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
async def get_users_me(
    current_user: dependency.GetCurrentUserDependency,
):
    """Get info about current user"""
<<<<<<< HEAD
<<<<<<< HEAD
    user = current_user
    return user

<<<<<<< HEAD
=======
    user = current_user
    return user
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
>>>>>>> e7f03f9 (Added docs)

@user_routers.patch("/me/", response_model=schemas.UserResponse)
async def update_user(
    session: dependency.AsyncSessionDependency,
    data: schemas.UserUpdate,
=======
    return current_user


@user_routers.patch("/me/", response_model=schemas.UserResponse)
async def update_user(
    session: dependency.AsyncSessionDependency,
<<<<<<< HEAD
    data: UserUpdate,
>>>>>>> 09b7086 (Add user routers)
=======
    data: schemas.UserUpdate,
>>>>>>> 3f2822f (Complete servis with admin and company)
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
