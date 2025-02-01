from datetime import date

import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrud


class TaskCrud(BaseCrud):
    """Execution of the request in database for task model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.Task

    async def get_yours_tasks(self, admin_id: int) -> list:
        """Get all tasks"""
        stmt = sa.select(self.model).where(
            self.model.tasks_user.any(user_id=admin_id)
        )
        response = await self.session.scalars(stmt)
        return response.unique().all()

    async def get_task(self, user_id: int, task_id: int) -> models.Task:
        """Get task by id"""
        stmt = (
            sa.select(self.model)
            .join(models.TaskUser, models.TaskUser.task_id == self.model.id)
            .where(
                models.TaskUser.user_id == user_id, self.model.id == task_id
            )
        )
        result = await self.session.execute(stmt)
        task = result.scalars().all()
        if len(task) == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You have not a permission to perform this action",
            )
        return task


class TaskUserCrud(BaseCrud):
    """Execution of the request in database for task-user model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.TaskUser


class MotivationCrud(BaseCrud):
    """Execution of the request in database for motivation model"""

    def __init__(self, session):
        super().__init__(session)
        self.model = models.Motivation

    async def get_grades(self, user_id: int, date_start: date, date_end: date):
        """Get grade for current user with date filter"""
        stmt = (
            sa.select(self.model.grade)
            .join(models.Task, models.Task.id == self.model.task_id)
            .where(
                self.model.user_id == user_id,
                models.Task.time >= date_start,
                models.Task.time <= date_end,
            )
        )
        result = await self.session.execute(stmt)
        grades = result.scalars().all()
        return grades

    async def get_company_grade(self, user_id: int):
        """Get grade for all company"""
        stmt = (
            sa.select(self.model.grade)
            .join(
                models.Organization,
                models.Organization.user_id == self.model.user_id,
            )
            .where(self.model.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        grades = result.scalars().all()
        return grades
