from typing import Any, Sequence

import sqlalchemy as sa
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

import database.models as models
from tests_config import utils
import datetime

faker = Faker()


class MainFactory:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.data: list[dict] = []
        self.model: models.TypeModel | None = None

    async def generate_data(self, count: int = 1, **kwargs):
        """
        Generate data for factory
        """
        raise NotImplementedError("Нужна реализация")

    async def insert_to_db(self) -> None:
        """
        Запись данных в БД
        """
        stmt = sa.insert(self.model).values(self.data)  # type:ignore[arg-type]
        await self.session.execute(stmt)

    async def get_data(self) -> Sequence[Any]:
        """
        Get data in DB
        """
        stmt = sa.select(self.model)  # type:ignore[arg-type]
        result = await self.session.scalars(stmt)
        return result.unique().all()


class UserFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.User

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.User]:
        self.data.extend(
            {
                "email": kwargs.get("email", faker.email()),
                "password": utils.hash_password(
                    kwargs.get("password", faker.password())
                ),
                "first_name": kwargs.get("first_name", faker.first_name()),
                "last_name": kwargs.get("last_name", faker.last_name()),
                "is_super_admin": kwargs.get("is_super_admin", False),
                "is_admin": kwargs.get("is_admin", False),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class CompanyFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.Company

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.Company]:
        self.data.extend(
            {
                "title": kwargs.get("title", faker.text()),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class OrganizationFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.Organization

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.Organization]:
        self.data.extend(
            {
                "company_id": kwargs.get("company_id", 1),
                "user_id": kwargs.get("user_id", 1),
                "role": kwargs.get("role", models.UserRole.SUPER_MANAGER),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class NewsFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.News

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.News]:
        self.data.extend(
            {
                "title": kwargs.get("title", faker.text()),
                "descriptions": kwargs.get("descriptions", faker.text()),
                "company_id": kwargs.get("company_id", 1),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class TaskFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.Task

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.Task]:
        self.data.extend(
            {
                "title": kwargs.get("title", faker.name()),
                "descriptions": kwargs.get("descriptions", faker.name()),
                "status": kwargs.get("status", models.TaskStatus.NEW),
                "comments": kwargs.get("comments", faker.name()),
                "time": kwargs.get("time", datetime.datetime.now()),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class TaskUserFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.TaskUser

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.TaskUser]:
        self.data.extend(
            {
                "user_id": kwargs.get("user_id", 1),
                "task_id": kwargs.get("task_id", 1),
                "user_role": kwargs.get(
                    "user_role", models.UserTaskRole.AUTHOR
                ),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class MotivationFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.Motivation

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.Motivation]:
        self.data.extend(
            {
                "task_id": kwargs.get("task_id", 1),
                "user_id": kwargs.get("user_id", 2),
                "grade": kwargs.get("grade", faker.random_number()),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class MeetingFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.Meeting

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.Meeting]:
        self.data.extend(
            {
                "title": kwargs.get("task_id", faker.name()),
                "date": kwargs.get("date", datetime.datetime.now()),
                "time": kwargs.get("time", datetime.time(hour=14, minute=25)),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()


class MeetingUserFactory(MainFactory):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = models.MeetingUser

    async def generate_data(
        self, count: int = 1, **kwargs
    ) -> Sequence[models.MeetingUser]:
        self.data.extend(
            {
                "meeting_id": kwargs.get("meeting_id", 1),
                "user_id": kwargs.get("user_id", 2),
            }
            for _ in range(count)
        )

        await self.insert_to_db()
        await self.session.commit()
        return await self.get_data()
