import sqlalchemy as sa
from database import models
<<<<<<< HEAD
<<<<<<< HEAD
from fastapi import HTTPException, status
from repository.base_crud import BaseCrudRestrict
from schemas import schemas
from sqlalchemy.exc import IntegrityError


class UserCrud(BaseCrudRestrict):
    """Execution of the request in database for user model"""

<<<<<<< HEAD
=======
=======
from fastapi import HTTPException, status
from repository.base_crud import BaseCrudRestrict
from sqlalchemy.exc import IntegrityError
>>>>>>> 3f2822f (Complete servis with admin and company)


class UserCrud(BaseCrudRestrict):
>>>>>>> 09b7086 (Add user routers)
=======
>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.User

    async def get_user(self, email: str) -> models.User:
<<<<<<< HEAD
<<<<<<< HEAD
        """Execution of the request get user by email"""
=======
>>>>>>> 09b7086 (Add user routers)
=======
        """Execution of the request get user by email"""
>>>>>>> e7f03f9 (Added docs)
        stmt = sa.select(self.model).where(self.model.email == email)
        user = await self.session.scalar(stmt)
        if user is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{email} not found"
            )
        return user
<<<<<<< HEAD
<<<<<<< HEAD


class JoinOrganizationCrud(BaseCrudRestrict):
    """Execution of the request for add user in company"""

<<<<<<< HEAD
=======


class JoinOrganizationCrud(BaseCrudRestrict):
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Organization

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e7f03f9 (Added docs)
    async def create_user_organization(
        self, data: schemas.JoinCompany
    ) -> models.Organization:
        """Execution of the request for add user in company"""
<<<<<<< HEAD
=======
    async def create_user_organization(self, data):
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
>>>>>>> e7f03f9 (Added docs)
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
<<<<<<< HEAD
=======
>>>>>>> 09b7086 (Add user routers)
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
