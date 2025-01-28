import sqlalchemy as sa
from database import models

from crud.base_crud import BaseCrudRestrict
from fastapi import status, HTTPException

class UserCrud(BaseCrudRestrict):
    def __init__(self, session):
        super().__init__(session)
        self.model = models.User

    async def get_user(self, email: str) -> models.User:
        stmt = sa.select(self.model).where(self.model.email == email)
        user = await self.session.scalar(stmt)
        if user is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{email} not found"
            )
        return user
