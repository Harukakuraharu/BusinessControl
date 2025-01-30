import json
from uuid import uuid4

from database import models
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from redis_cli.redis_client import redis_client
from sqlalchemy.ext.asyncio import AsyncSession

from crud.admin_crud import AdminCrud, CompanyCrud, NewsCrud, OrganizationCrud


class AdminServices:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud_user = AdminCrud(self.session)
        self.crud_organization = OrganizationCrud(self.session)
        self.crud_news = NewsCrud(self.session)

    async def update_admin_status(self, current_user, data):
        if current_user.is_super_admin is not True:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You have not a permission to perform this action",
            )
        user = await self.crud_user.get_user(data.email)
        user.is_admin = True
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def add_user(self, data, admin):
        user = await self.crud_user.get_user(data.email)
        if user.organization is not None:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "User already exists in some organization",
            )
        create_data = {
            "role": data.role,
            "user_id": user.id,
            "company_id": admin.organization.company_id,
        }
        organization = await self.crud_organization.create_item(create_data)
        await self.session.commit()
        await self.session.refresh(organization)
        return organization

    async def remove_user(self, data, admin):
        user = await self.crud_user.get_user(data.email)
        if (
            user.organization is None
            or user.organization.company_id != admin.organization.company_id
        ):
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                "User not exists is this organization",
            )

        await self.crud_organization.delete_item(user.organization.id)
        await self.session.commit()
        return JSONResponse(
            content="Successfully deleted", status_code=status.HTTP_200_OK
        )

    async def get_news(self, admin, news_id):
        news = await self.crud_news.check_owner(
            news_id, admin.organization.company_id
        )
        return news

    async def get_all_news(self, admin):
        news = await self.crud_news.get_all_news(admin.organization.company_id)
        return news

    async def add_news(self, create_data, admin):
        data = create_data.model_dump()
        data["company_id"] = admin.organization.company_id
        news = await self.crud_news.create_item(data)
        await self.session.commit()
        await self.session.refresh(news)
        return news

    async def update_news(self, update_data, admin, news_id):
        data = update_data.model_dump(exclude_unset=True)
        data["id"] = news_id
        await self.crud_news.check_owner(
            admin.organization.company_id, news_id
        )
        result = await self.crud_news.update_item(data)
        await self.session.commit()
        await self.session.refresh(result)
        return result

    async def delete_news(self, admin, news_id):
        await self.crud_news.check_owner(
            admin.organization.company_id, news_id
        )
        await self.crud_news.delete_item(news_id)
        await self.session.commit()
        return JSONResponse(
            content="Successfully deleted", status_code=status.HTTP_200_OK
        )


class CompanyServices:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud = CompanyCrud(self.session)
        self.crud_organization = OrganizationCrud(self.session)

    async def create_company(self, data, admin):
        if admin.organization is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have a company",
            )
        company = await self.crud.create_item(data.model_dump())
        await self.crud_organization.create_item(
            {
                "company_id": company.id,
                "user_id": admin.id,
                "role": models.UserRole.SUPER_MANAGER,
            }
        )
        await self.session.commit()
        await self.session.refresh(company)
        return company

    async def get_company(self, user):
        company = await self.crud.get_company(user)
        return company

    async def update_company(self, user, update_data):
        data = update_data.model_dump()
        data["id"] = user.organization.company_id
        company = await self.crud.update_item(data)
        await self.session.commit()
        await self.session.refresh(company)
        return company

    async def delete_company(self, user):
        await self.crud.delete_item(user.organization.company_id)
        await self.session.commit()
        return JSONResponse(
            content="Successfully deleted", status_code=status.HTTP_200_OK
        )


class RedisServise:
    async def create_code(self, admin, data):
        code = str(uuid4())
        set_data = {
            "company_id": admin.organization.company_id,
            "role": data.role.value,
        }
        redis_client.set(code, json.dumps(set_data), ex=1000)
        return code
