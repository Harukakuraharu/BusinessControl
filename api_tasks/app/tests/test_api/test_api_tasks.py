import pytest
from database import models
from fastapi import status
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from tests_config import factory as fc


pytestmark = pytest.mark.anyio


async def test_create_task_manager(admin_company_client: AsyncClient):
    """Create task by manager or admin"""
    data = {
        "title": "Hello",
        "descriptions": "How are you",
        "status": models.TaskStatus.NEW.value,
<<<<<<< HEAD
<<<<<<< HEAD
        "date": "10:00",
=======
        "time": "10:00",
>>>>>>> 6230ac8 (Added api tests)
=======
        "date": "10:00",
>>>>>>> 0f0357a (Fix migrations and tests)
    }
    response = await admin_company_client.post("/tasks/", json=data)
    assert response.status_code == status.HTTP_200_OK


async def test_create_task_user(user_client: AsyncClient):
    """Create task by employeer or if user do not have company"""
    data = {
        "title": "Hello",
        "descriptions": "How are you",
        "status": models.TaskStatus.NEW.value,
<<<<<<< HEAD
<<<<<<< HEAD
        "date": "10:00",
=======
        "time": "10:00",
>>>>>>> 6230ac8 (Added api tests)
=======
        "date": "10:00",
>>>>>>> 0f0357a (Fix migrations and tests)
    }
    response = await user_client.post("/tasks/", json=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_add_user_task(
    admin_company_client: AsyncClient, factory, async_session: AsyncSession
):
    """Test add task for user by admin"""
    user = await factory(fc.UserFactory)
    task = await factory(fc.TaskFactory)
    await factory(fc.TaskUserFactory, task_id=task.id)
    await async_session.refresh(user[1])
    data = {
        "task_id": task.id,
        "user_id": user[1].id,
        "user_role": models.UserTaskRole.WORKER.value,
    }
    response = await admin_company_client.post("/tasks/add_user/", json=data)
    assert response.status_code == status.HTTP_200_OK


async def test_get_all_manager_tasks(
    admin_company_client: AsyncClient, factory, async_session: AsyncSession
):
    """Test get all tasks for manager"""
    count = 2
    tasks = await factory(fc.TaskFactory, count, user_id=1)
    await factory(fc.TaskUserFactory, task_id=tasks[0].id)
    await async_session.refresh(tasks[1])
    await factory(fc.TaskUserFactory, task_id=tasks[1].id)
    response = await admin_company_client.get("/tasks/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


async def test_get_manager_task(admin_company_client: AsyncClient, factory):
    """Test get tasks for manager with id"""
    task = await factory(fc.TaskFactory, user_id=1)
    await factory(fc.TaskUserFactory, task_id=task.id)
    response = await admin_company_client.get(f"/tasks/{task.id}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


async def test_update_task_manager(admin_company_client: AsyncClient, factory):
    """Test update tasks for manager"""
    data = {
        "descriptions": "Hehehehe",
    }
    task = await factory(fc.TaskFactory, user_id=1)
    await factory(fc.TaskUserFactory, task_id=task.id)
    response = await admin_company_client.patch(f"/tasks/{task.id}", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["descriptions"] == data["descriptions"]


async def test_update_task_user(user_client: AsyncClient, factory):
    """Test update tasks for employee"""
    data = {
        "descriptions": "Hehehehe",
    }
    task = await factory(fc.TaskFactory, user_id=1)
    await factory(fc.TaskUserFactory, task_id=task.id)
    response = await user_client.patch(f"/tasks/{task.id}", json=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_delete_task_manager(admin_company_client: AsyncClient, factory):
    """Test delete tasks for manager"""
    task = await factory(fc.TaskFactory, user_id=1)
    await factory(fc.TaskUserFactory, task_id=task.id)
    response = await admin_company_client.delete(f"/tasks/{task.id}")
    assert response.status_code == status.HTTP_200_OK


async def test_update_task_employee(
    user_company_client: AsyncClient, factory, async_session: AsyncSession
):
    """Test update tasks status and comment for employee"""
    data = {
        "status": models.TaskStatus.DONE.value,
    }
    users = await factory(fc.UserFactory, is_admin=True)
    user = users[0]
    admin = users[1]
    task = await factory(fc.TaskFactory, user_id=admin.id)
    await async_session.refresh(admin)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=admin.id)
    await async_session.refresh(user)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=user.id)
    response = await user_company_client.patch(
        f"tasks/task_status/{task.id}/", json=data
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == data["status"]


async def test_create_grade_task(
    admin_company_client: AsyncClient, factory, async_session: AsyncSession
):
    """Create grade for task"""
    users = await factory(fc.UserFactory)
    admin = users[0]
    user = users[1]
    data = {"grade": 85, "user_id": user.id}
    task = await factory(fc.TaskFactory, user_id=admin.id)
    await async_session.refresh(admin)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=admin.id)
    await async_session.refresh(user)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=user.id)
    response = await admin_company_client.post(
        f"tasks/grade/{task.id}/", json=data
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["grade"] == data["grade"]


async def test_get_avg_employee(
    user_company_client: AsyncClient, factory, async_session: AsyncSession
):
    """Test get avg grade tasks for employee"""
    grade = 50
    users = await factory(fc.UserFactory, is_admin=True)
    user = users[0]
    admin = users[1]
    task = await factory(fc.TaskFactory, user_id=admin.id)
    await async_session.refresh(admin)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=admin.id)
    await async_session.refresh(user)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=user.id)
    await factory(
        fc.MotivationFactory, task_id=task.id, user_id=user.id, grade=grade
    )
    response = await user_company_client.get(
        "tasks/grade/",
        params={"date_start": "2025-01-01", "date_end": "2025-02-10"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == grade


async def test_get_company_grade(
    user_company_client: AsyncClient, factory, async_session: AsyncSession
):
    """Test get company grade tasks for employee"""
    grade = 35
    users = await factory(fc.UserFactory, is_admin=True)
    user = users[0]
    admin = users[1]
    task = await factory(fc.TaskFactory, user_id=admin.id)
    await async_session.refresh(admin)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=admin.id)
    await async_session.refresh(user)
    await factory(fc.TaskUserFactory, task_id=task.id, user_id=user.id)
    await factory(
        fc.MotivationFactory, task_id=task.id, user_id=user.id, grade=grade
    )
    response = await user_company_client.get("tasks/grade/company/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == grade
