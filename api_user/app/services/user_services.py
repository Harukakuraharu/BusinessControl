from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import security
from app.core.settings import config
from app.crud.user_crud import UserCrud

from schemas.users import Token


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud = UserCrud(self.session)

    async def create_user(self, data):
        data.password = security.hash_password(data.password)
        try:
            user = await UserCrud(self.session).create_or_update(
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

    async def login(self, data):
        user = await security.auth(self.session, data.email, data.password)
        access_token_expires = timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        access_token = security.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token)

    async def update_user(self, data, current_user):
        update_data = data.model_dump(exclude_unset=True)
        update_data["id"] = current_user.id
        user = await UserCrud(self.session).create_or_update(
            update_data, "update"
        )
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete_user(self, current_user):
        await UserCrud(self.session).delete_item(current_user.id)
        await self.session.commit()
