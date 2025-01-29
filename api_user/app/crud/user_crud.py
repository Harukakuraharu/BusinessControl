import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrudRestrict
from sqlalchemy.exc import IntegrityError


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


class JoinOrganizationCrud(BaseCrudRestrict):
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Organization

    async def create_user_organization(self, data):
        try:
            stmt = (
                sa.insert(models.Organization)
                .returning(models.Organization)
                .values(**data)
            )
            organization = await self.session.scalar(stmt)
            await self.session.commit()
            await self.session.refresh(organization)
        except IntegrityError as error:
            if error.orig is not None and "uq_" in error.orig.args[0]:
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    "User already exists",
                ) from error
            raise error
        return organization
