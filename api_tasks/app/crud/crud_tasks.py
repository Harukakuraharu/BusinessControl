from datetime import date

import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrud


class TaskCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for task model"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Execution of the request in database for task model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Task

<<<<<<< HEAD
<<<<<<< HEAD
    async def get_yours_tasks(self, admin_id: int) -> list:
        """Get all tasks"""
=======
    async def get_yours_tasks(self, admin_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    async def get_yours_tasks(self, admin_id: int) -> list:
        """Get all tasks"""
>>>>>>> e7f03f9 (Added docs)
        stmt = sa.select(self.model).where(
            self.model.tasks_user.any(user_id=admin_id)
        )
        response = await self.session.scalars(stmt)
        return response.unique().all()

<<<<<<< HEAD
<<<<<<< HEAD
    async def get_task(self, user_id: int, task_id: int) -> models.Task:
        """Get task by id"""
=======
    async def get_task(self, user_id: int, task_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    async def get_task(self, user_id: int, task_id: int) -> models.Task:
        """Get task by id"""
>>>>>>> e7f03f9 (Added docs)
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
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for task-user model"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Execution of the request in database for task-user model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.TaskUser


class MotivationCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for motivation model"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Execution of the request in database for motivation model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Motivation

    async def get_grades(self, user_id: int, date_start: date, date_end: date):
<<<<<<< HEAD
<<<<<<< HEAD
        """Get grade for current user with date filter"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
        """Get grade for current user with date filter"""
>>>>>>> e7f03f9 (Added docs)
        stmt = (
            sa.select(self.model.grade)
            .join(models.Task, models.Task.id == self.model.task_id)
            .where(
                self.model.user_id == user_id,
<<<<<<< HEAD
                models.Task.date >= date_start,
                models.Task.date <= date_end,
=======
                models.Task.time >= date_start,
                models.Task.time <= date_end,
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
            )
        )
        result = await self.session.execute(stmt)
        grades = result.scalars().all()
        return grades

    async def get_company_grade(self, user_id: int):
<<<<<<< HEAD
<<<<<<< HEAD
        """Get grade for all company"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
        """Get grade for all company"""
>>>>>>> e7f03f9 (Added docs)
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
