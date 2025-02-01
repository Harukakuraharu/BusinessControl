<<<<<<< HEAD
<<<<<<< HEAD
from core import dependency
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
from services.services_tasks import TaskServices

=======
=======
from core import dependency
>>>>>>> e7f03f9 (Added docs)
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
from services.services_tasks import TaskServices

>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
tasks_routers = APIRouter(prefix="/tasks", tags=["Tasks"])


@tasks_routers.post("/", response_model=schemas.CreateTaskResponse)
async def create_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    data: schemas.CreateTask,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Create task by company admin"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Create task by company admin"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).create_task(admin, data)


@tasks_routers.post("/add_user/", response_model=schemas.AddUserTaskResponse)
async def add_user_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    data: schemas.AddUserTask,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Add user in task"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Add user in task"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).add_user_task(data, admin.id)


@tasks_routers.get("/", response_model=list[schemas.TaskResponse])
async def get_all_yours_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Get all tasks"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Get all tasks"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).get_tasks(admin.id)


@tasks_routers.get("/{task_id}", response_model=list[schemas.TaskResponse])
async def get_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Get task by id"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Get task by id"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).get_task(admin.id, task_id)


@tasks_routers.patch("/{task_id}", response_model=schemas.TaskResponse)
async def update_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
    data: schemas.TaskUpdate,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Update task"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Update task"""
>>>>>>> e7f03f9 (Added docs)
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
<<<<<<< HEAD
<<<<<<< HEAD
    "/task_status/{task_id}/", response_model=schemas.TaskStatusUpdateResponse
=======
    "/task_status/{task_id}", response_model=schemas.TaskStatusUpdateResponse
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    "/task_status/{task_id}/", response_model=schemas.TaskStatusUpdateResponse
>>>>>>> 6230ac8 (Added api tests)
)
async def update_status_task(
    session: dependency.AsyncSessionDependency,
    data: schemas.TaskStatusUpdate,
    user: dependency.GetCurrentUserDependency,
    task_id: int,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Update task status"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Update task status"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).update_task_status(
        task_id, data, user.id
    )


@tasks_routers.post(
<<<<<<< HEAD
<<<<<<< HEAD
    "/grade/{task_id}/", response_model=schemas.CreateGradeResponse
=======
    "/grade/{task_id}", response_model=schemas.CreateGradeResponse
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    "/grade/{task_id}/", response_model=schemas.CreateGradeResponse
>>>>>>> 6230ac8 (Added api tests)
)
async def create_grade_task(
    session: dependency.AsyncSessionDependency,
    admin: dependency.ManagerPermissionDependency,
    task_id: int,
    data: schemas.CreareGrade,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Create grade for task by tasks owner"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Create grade for task by tasks owner"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).create_grade(task_id, data, admin.id)


@tasks_routers.get("/grade/")
async def get_grade_task(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
    params: schemas.GetGrade = Depends(),
):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e7f03f9 (Added docs)
    """Get grade for task"""
    return await TaskServices(session).get_param_grade(user.id, params)
=======
    return await TaskServices(session).get_param_grade(user, params)
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    return await TaskServices(session).get_param_grade(user.id, params)
>>>>>>> 6230ac8 (Added api tests)


@tasks_routers.get("/grade/company/")
async def get_grade_company(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
):
<<<<<<< HEAD
<<<<<<< HEAD
    """Get grade task for all conpany"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Get grade task for all conpany"""
>>>>>>> e7f03f9 (Added docs)
    return await TaskServices(session).get_company_grade(user.id)
