import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrud


class AdminCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for user model"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Execution of the request in database for user model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.User

    async def get_user(self, email: str) -> models.User:
<<<<<<< HEAD
<<<<<<< HEAD
        """Get user in database with email"""
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
        """Get user in database with email"""
>>>>>>> e7f03f9 (Added docs)
        stmt = sa.select(self.model).where(self.model.email == email)
        user = await self.session.scalar(stmt)
        if user is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{self.model.__name__} not found"
            )
        return user


class CompanyCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for company model"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Execution of the request in database for company model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Company

<<<<<<< HEAD
<<<<<<< HEAD
    async def get_company(self, user: models.User) -> models.Company:
        """Get users company on database"""
=======
    async def get_company(self, user):
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    async def get_company(self, user: models.User) -> models.Company:
        """Get users company on database"""
>>>>>>> e7f03f9 (Added docs)
        if user.organization is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{self.model.__name__} not found"
            )
        stmt = sa.select(self.model).where(
            self.model.id == user.organization.company_id
        )
        company = await self.session.scalar(stmt)
        return company


class OrganizationCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for organization model"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Execution of the request in database for organization model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Organization


class NewsCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for news model"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Execution of the request in database for news model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.News

<<<<<<< HEAD
<<<<<<< HEAD
    async def check_owner(self, news_id: int, company_id: int) -> list:
        """Check news owner"""
=======
    async def check_owner(self, news_id: int, company_id: int):
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    async def check_owner(self, news_id: int, company_id: int) -> list:
        """Check news owner"""
>>>>>>> e7f03f9 (Added docs)
        news = await self.get_item_id(news_id)
        if news is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "News not found")
        stmt = sa.select(self.model).where(self.model.company_id == company_id)
        result = await self.session.scalar(stmt)
        if result is None:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN, f"{self.model.__name__} not yours"
            )
        return result

<<<<<<< HEAD
<<<<<<< HEAD
    async def get_all_news(self, item_id: int) -> list:
        """Get owner news"""
=======
    async def get_all_news(self, item_id: int):
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    async def get_all_news(self, item_id: int) -> list:
        """Get owner news"""
>>>>>>> e7f03f9 (Added docs)
        stmt = sa.select(self.model).where(self.model.company_id == item_id)
        result = await self.session.scalars(stmt)
        return result.unique().all()
