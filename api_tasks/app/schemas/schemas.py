import datetime

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CreateTask(BaseModel):
    title: str
    descriptions: str
    status: models.TaskStatus


class TaskUser(BaseModel):
    id: int
    user_id: int
    task_id: int
    user_role: models.UserTaskRole


class CreateTaskResponse(CreateTask):
    time: datetime.date
    tasks_user: list[TaskUser]


class AddUserTask(BaseModel):
    task_id: int
    user_id: int
    user_role: models.UserTaskRole


class AddUserTaskResponse(AddUserTask):
    id: int


class TaskResponse(CreateTask):
    id: int
    time: datetime.date
    tasks_user: list[TaskUser]


class TaskUpdate(BaseModel):
    title: str | None = None
    descriptions: str | None = None


class TaskStatusUpdate(BaseModel):
    status: models.TaskStatus | None = None
    comments: str | None = None


class TaskStatusUpdateResponse(BaseModel):
    status: models.TaskStatus
    comments: str
    title: str
    descriptions: str


class CreareGrade(BaseModel):
    user_id: int
    grade: int


class CreateGradeResponse(CreareGrade):
    id: int


class GetGrade(BaseModel):
    date_start: datetime.date
    date_end: datetime.date


class MeetingUser(BaseModel):
    user_id: int


class CreateMeeting(BaseModel):
    title: str
    date: datetime.date
    time: datetime.time


class CreateMeetingResponse(CreateMeeting):
    id: int
    meeting_user: list[MeetingUser]


class UpdateMeeting(BaseModel):
    title: str | None = None
    date: datetime.date | None = None
    time: datetime.time | None = None


class AddUserMeeting(BaseModel):
    user_id: int
    meeting_id: int


class AddUserMeetingResponse(AddUserMeeting):
    meetings: CreateMeeting
