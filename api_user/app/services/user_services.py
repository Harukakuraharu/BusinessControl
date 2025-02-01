import json
from datetime import timedelta

import sqlalchemy as sa
from core import security
from core.settings import config
from crud.user_crud import JoinOrganizationCrud, UserCrud
from database import models
from fastapi import HTTPException, status
from redis_cli.redis_client import redis_client
from schemas import schemas
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from tests_config import utils


class UserService:
    """Execution of the request for user endpoint"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud = UserCrud(self.session)
        self.organization_crud = JoinOrganizationCrud(self.session)

    async def create_user(self, data: schemas.UserCreate) -> models.User:
        """Execution of the request for create user"""
        data.password = utils.hash_password(data.password)
        try:
            user = await self.crud.create_or_update(
                data.model_dump(), "create"
            )
            await self.session.commit()
            await self.session.refresh(user)
        except IntegrityError as error:
            if error.orig is not None and "uq_" in error.orig.args[0]:
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    "User already exists",
                ) from error
            raise error
        return user

    async def login(self, data: schemas.UserLogin) -> schemas.Token:
        """Execution of the request for login user"""
        user = await security.auth(self.session, data.email, data.password)
        access_token_expires = timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        access_token = utils.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return schemas.Token(access_token=access_token)

    async def update_user(
        self, data: schemas.UserUpdate, current_user: models.User
    ) -> models.User:
        """Execution of the request for update user"""
        update_data = data.model_dump(exclude_unset=True)
        update_data["id"] = current_user.id
        user = await self.crud.create_or_update(update_data, "update")
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete_user(self, current_user: models.User) -> None:
        """Execution of the request for delete user"""
        await self.crud.delete_item(current_user.id)
        await self.session.commit()

    async def join_company(
        self, current_user: models.User, user_data: schemas.JoinCompany
    ):
        """Execution of the request for add user on company"""
        code = redis_client.get(user_data.code)
        if code is None:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Incorrect code",
            )
        data = json.loads(code)
        if data["role"] == "manager":
            data["role"] = models.UserRole.MANAGER
        else:
            data["role"] = models.UserRole.EMPLOYEE
        create_data = {
            "user_id": current_user.id,
            "company_id": data["company_id"],
            "role": data["role"],
        }
        result = await self.organization_crud.create_user_organization(
            create_data
        )
        return result
