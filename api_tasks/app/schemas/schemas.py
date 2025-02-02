import datetime

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    """Main schemas for user"""

    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
    """Main response schemas for user"""

    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CreateTask(BaseModel):
    """Schemas for create task"""

    title: str
    descriptions: str
    status: models.TaskStatus


class TaskUser(BaseModel):
    """Schemas for tasks_user field on CreateTaskResponse schemas"""

    id: int
    user_id: int
    task_id: int
    user_role: models.UserTaskRole


class CreateTaskResponse(CreateTask):
    """Response schemas for create tasks"""

    date: datetime.date
    tasks_user: list[TaskUser]


class AddUserTask(BaseModel):
    """Schemas for add user in tasks"""

    task_id: int
    user_id: int
    user_role: models.UserTaskRole


class AddUserTaskResponse(AddUserTask):
    """Response schemas for add user in tasks"""

    id: int


class TaskResponse(CreateTask):
    """Schemas for get tasks"""

    id: int
    date: datetime.date
    tasks_user: list[TaskUser]


class TaskUpdate(BaseModel):
    """Schemas for update response"""

    title: str | None = None
    descriptions: str | None = None


class TaskStatusUpdate(BaseModel):
    """Schemas for update tasks status or comment"""

    status: models.TaskStatus | None = None
    comments: str | None = None


class TaskStatusUpdateResponse(BaseModel):
    """Response schemas for update tasks status or comment"""

    status: models.TaskStatus
    comments: str
    title: str
    descriptions: str


class CreareGrade(BaseModel):
    """Schemas foor create grade tasks"""

    user_id: int
    grade: int


class CreateGradeResponse(CreareGrade):
    """Response schemas foor create grade tasks"""

    id: int


class GetGrade(BaseModel):
    """Schemas for get grade woth date filters"""

    date_start: datetime.date
    date_end: datetime.date


class MeetingUser(BaseModel):
    """Schemas for meeting for user"""

    user_id: int


class CreateMeeting(BaseModel):
    """Schemas for create meeting"""

    title: str
    date: datetime.date
    time: datetime.time


class CreateMeetingResponse(CreateMeeting):
    """Response schemas for create meeting"""

    id: int
    meeting_user: list[MeetingUser]


class UpdateMeeting(BaseModel):
    """Schemas for update meeting"""

    title: str | None = None
    date: datetime.date | None = None
    time: datetime.time | None = None


class AddUserMeeting(BaseModel):
    """Schemas for add user for meeting"""

    user_id: int
    meeting_id: int


class AddUserMeetingResponse(AddUserMeeting):
    """Response schemas for add user for meeting"""

    meetings: CreateMeeting
