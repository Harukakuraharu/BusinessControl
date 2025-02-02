from core import dependency
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
from services.services_tasks import TaskServices

tasks_routers = APIRouter(prefix="/tasks", tags=["Tasks"])


@tasks_routers.post("/", response_model=schemas.CreateTaskResponse)
async def create_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    data: schemas.CreateTask,
):
    """Create task by company admin"""
    return await TaskServices(session).create_task(admin, data)


@tasks_routers.post("/add_user/", response_model=schemas.AddUserTaskResponse)
async def add_user_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    data: schemas.AddUserTask,
):
    """Add user in task"""
    return await TaskServices(session).add_user_task(data, admin.id)


@tasks_routers.get("/", response_model=list[schemas.TaskResponse])
async def get_all_yours_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
):
    """Get all tasks"""
    return await TaskServices(session).get_tasks(admin.id)


@tasks_routers.get("/{task_id}", response_model=list[schemas.TaskResponse])
async def get_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
):
    """Get task by id"""
    return await TaskServices(session).get_task(admin.id, task_id)


@tasks_routers.patch("/{task_id}", response_model=schemas.TaskResponse)
async def update_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
    data: schemas.TaskUpdate,
):
    """Update task"""
    return await TaskServices(session).update_task(admin.id, task_id, data)


@tasks_routers.delete("/{task_id}")
async def delete_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
):
    await TaskServices(session).delete_task(admin.id, task_id)
    return JSONResponse(
        content="Successfully deleted", status_code=status.HTTP_200_OK
    )


@tasks_routers.patch(
    "/task_status/{task_id}/", response_model=schemas.TaskStatusUpdateResponse
)
async def update_status_task(
    session: dependency.AsyncSessionDependency,
    data: schemas.TaskStatusUpdate,
    user: dependency.GetCurrentUserDependency,
    task_id: int,
):
    """Update task status"""
    return await TaskServices(session).update_task_status(
        task_id, data, user.id
    )


@tasks_routers.post(
    "/grade/{task_id}/", response_model=schemas.CreateGradeResponse
)
async def create_grade_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
    data: schemas.CreareGrade,
):
    """Create grade for task by tasks owner"""
    return await TaskServices(session).create_grade(task_id, data, admin.id)


@tasks_routers.get("/grade/")
async def get_grade_task(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
    params: schemas.GetGrade = Depends(),
):
    """Get grade for task"""
    return await TaskServices(session).get_param_grade(user.id, params)


@tasks_routers.get("/grade/company/")
async def get_grade_company(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
):
    """Get grade task for all conpany"""
    return await TaskServices(session).get_company_grade(user.id)
