import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrudRestrict
from schemas import schemas
from sqlalchemy.exc import IntegrityError


class UserCrud(BaseCrudRestrict):
    """Execution of the request in database for user model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.User

    async def get_user(self, email: str) -> models.User:
        """Execution of the request get user by email"""
        stmt = sa.select(self.model).where(self.model.email == email)
        user = await self.session.scalar(stmt)
        if user is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{email} not found"
            )
        return user


class JoinOrganizationCrud(BaseCrudRestrict):
    """Execution of the request for add user in company"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.Organization

    async def create_user_organization(
        self, data: schemas.JoinCompany
    ) -> models.Organization:
        """Execution of the request for add user in company"""
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
