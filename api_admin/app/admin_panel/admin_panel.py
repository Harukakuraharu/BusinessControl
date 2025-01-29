import httpx
from database import models
from fastapi import HTTPException, status
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from starlette.requests import Request

from core.settings import config
from crud.admin_crud import AdminCrud


class AdminAuth(AuthenticationBackend):
<<<<<<< HEAD
    """Get access token and auth user for login in admin panel"""

    async def login(self, request: Request) -> bool:
        """Login in admin-panel"""
=======
    async def login(self, request: Request) -> bool:
>>>>>>> 3f2822f (Complete servis with admin and company)
        form = await request.form()
        email, password = form["username"], form["password"]
        response = httpx.post(
            "http://127.0.0.1:8000/user/auth/",
            json={"email": email, "password": password},
        )
        if response.status_code == 404:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
        request.session.update(
            {"access_token": f"{response.json()["access_token"]}"}
        )
        async with AsyncSession(
            create_async_engine(config.async_dsn)  # type: ignore[arg-type]
        ) as session:
<<<<<<< HEAD
            user = await AdminCrud(session).get_user(
                email  # type: ignore[arg-type]
            )
=======
            user = await AdminCrud(session).get_user(email)
>>>>>>> 3f2822f (Complete servis with admin and company)
            if user.is_admin is not True:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You have not a permission to perform this action",
                )
        return True

    async def logout(self, request: Request) -> bool:
<<<<<<< HEAD
        """Logout in admin panel"""
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
<<<<<<< HEAD
        """Check token in curent user for admin panel"""
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
        token = request.session.get("access_token")
        if not token:
            return False
        return True


authentication_backend = AdminAuth(secret_key="")


class CompanyAdmin(ModelView, model=models.Company):
<<<<<<< HEAD
    """Table for company model in admin panel"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    column_list = [
        models.Company.id,
        models.Company.title,
        models.Company.organization,
        models.Company.news,
    ]


class NewsAdmin(ModelView, model=models.News):
<<<<<<< HEAD
    """Table for news model in admin panel"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    column_list = [
        models.News.id,
        models.News.title,
        models.News.descriptions,
        models.News.company,
    ]
    column_searchable_list = [models.News.title]


class OrganizationAdmin(ModelView, model=models.Organization):
<<<<<<< HEAD
    """Table for organization model in admin panel"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    column_list = [
        models.Organization.id,
        models.Organization.company_id,
        models.Organization.user_id,
        models.Organization.company,
        models.Organization.user,
    ]
