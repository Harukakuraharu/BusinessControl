from database import models
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from crud import crud_tasks as crud
from schemas import schemas


class TaskServices:
    """Execution of the request for tasks endpoint"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud_task = crud.TaskCrud(self.session)
        self.crud_task_user = crud.TaskUserCrud(self.session)
        self.crud_motivation = crud.MotivationCrud(self.session)

    async def create_task(
        self, admin: models.User, data: schemas.CreateTask
    ) -> models.Task:
        """Execution of the request for create task"""
        task = await self.crud_task.create_item(data.model_dump())
        task_data = {
            "user_id": admin.id,
            "user_role": models.UserTaskRole.AUTHOR,
            "task_id": task.id,
        }
        await self.crud_task_user.create_item(task_data)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def add_user_task(
        self, data: schemas.AddUserTask, admin_id: int
    ) -> models.TaskUser:
        """Execution of the request for add task for user"""
        await self.crud_task.get_task(admin_id, data.task_id)
        task_user_data = {
            "task_id": data.task_id,
            "user_id": data.user_id,
            "user_role": data.user_role,
        }
        try:
            task_user = await self.crud_task_user.create_item(task_user_data)
            await self.session.commit()
        except IntegrityError as error:
            if error.orig is not None and "uq_" in error.orig.args[0]:
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    "User already exists in this task",
                ) from error
            raise error
        await self.session.refresh(task_user)
        return task_user

    async def get_tasks(self, admin_id: int) -> list:
        """Execution of the request for get all tasks"""
        tasks = await self.crud_task.get_yours_tasks(admin_id)
        return tasks

    async def get_task(self, admin_id: int, task_id: int) -> models.Task:
        """Execution of the request for get task by id"""
        task = await self.crud_task.get_task(admin_id, task_id)
        return task

    async def update_task(
        self, admin_id: int, task_id: int, update_data: schemas.TaskUpdate
    ) -> models.Task:
        """Execution of the request for update task"""
        await self.crud_task.get_task(admin_id, task_id)
        data = update_data.model_dump(exclude_unset=True)
        data["id"] = task_id
        task = await self.crud_task.update_item(data)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete_task(self, admin_id: int, task_id: int) -> None:
        """Execution of the request for delete task"""
        await self.crud_task.get_task(admin_id, task_id)
        await self.crud_task.delete_item(task_id)
        await self.session.commit()

    async def update_task_status(
        self, task_id: int, update_data: schemas.TaskStatusUpdate, user_id: int
    ) -> models.Task:
        """Execution of the request for update task status or comment"""
        await self.crud_task.get_task(user_id, task_id)
        data = update_data.model_dump(exclude_unset=True)
        data["id"] = task_id
        task = await self.crud_task.update_item(data)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def create_grade(
        self, task_id: int, data: schemas.CreareGrade, user_id: int
    ) -> models.Motivation:
        """Execution of the request for create grade task"""
        await self.crud_task.get_task(user_id, task_id)
        create_data = data.model_dump()
        create_data["task_id"] = task_id
        try:
            grade = await self.crud_motivation.create_item(create_data)
            await self.session.commit()
        except IntegrityError as error:
            if error.orig is not None and "uq_" in error.orig.args[0]:
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    "User already exists in this task",
                ) from error
            raise error
        await self.session.refresh(grade)
        return grade

    async def get_param_grade(
        self, user_id: int, params: schemas.GetGrade
    ) -> list:
        """Execution of the request for get grade task"""
        data = params.model_dump()
        date_start = data.pop("date_start")
        date_end = data.pop("date_end")
        grade = await self.crud_motivation.get_grades(
            user_id, date_start, date_end
        )
        if len(grade) == 0:
            return grade
        return sum(grade) / len(grade)

    async def get_company_grade(self, user_id: int) -> list:
        """Execution of the request for create grade task for company"""
        grade = await self.crud_motivation.get_company_grade(user_id)
        if len(grade) == 0:
            return grade
        return sum(grade) / len(grade)
