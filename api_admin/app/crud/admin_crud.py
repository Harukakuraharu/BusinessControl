import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrud


class AdminCrud(BaseCrud):
    def __init__(self, session):
        super().__init__(session)
        self.model = models.User

    async def get_user(self, email: str) -> models.User:
        stmt = sa.select(self.model).where(self.model.email == email)
        user = await self.session.scalar(stmt)
        if user is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"{self.model.__name__} not found"
            )
        return user


class CompanyCrud(BaseCrud):
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Company

    async def get_company(self, user):
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
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Organization


class NewsCrud(BaseCrud):
    def __init__(self, session):
        super().__init__(session)
        self.model = models.News

    async def check_owner(self, news_id: int, company_id: int):
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

    async def get_all_news(self, item_id: int):
        stmt = sa.select(self.model).where(self.model.company_id == item_id)
        result = await self.session.scalars(stmt)
        return result.unique().all()
