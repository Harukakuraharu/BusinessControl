import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrud


class AdminCrud(BaseCrud):
    """Execution of the request in database for user model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.User

    async def get_user(self, email: str) -> models.User:
        """Get user in database with email"""
        stmt = sa.select(self.model).where(self.model.email == email)
        user = await self.session.scalar(stmt)
        if user is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{self.model.__name__} not found"
            )
        return user


class CompanyCrud(BaseCrud):
    """Execution of the request in database for company model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.Company

    async def get_company(self, user: models.User) -> models.Company:
        """Get users company on database"""
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
    """Execution of the request in database for organization model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.Organization


class NewsCrud(BaseCrud):
    """Execution of the request in database for news model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.News

    async def check_owner(self, news_id: int, company_id: int) -> list:
        """Check news owner"""
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

    async def get_all_news(self, item_id: int) -> list:
        """Get owner news"""
        stmt = sa.select(self.model).where(self.model.company_id == item_id)
        result = await self.session.scalars(stmt)
        return result.unique().all()
