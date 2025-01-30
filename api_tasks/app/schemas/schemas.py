import datetime

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
<<<<<<< HEAD
    """Main schemas for user"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
<<<<<<< HEAD
    """Main response schemas for user"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CreateTask(BaseModel):
<<<<<<< HEAD
    """Schemas for create task"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    title: str
    descriptions: str
    status: models.TaskStatus


class TaskUser(BaseModel):
<<<<<<< HEAD
    """Schemas for tasks_user field on CreateTaskResponse schemas"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    id: int
    user_id: int
    task_id: int
    user_role: models.UserTaskRole


class CreateTaskResponse(CreateTask):
<<<<<<< HEAD
    """Response schemas for create tasks"""

    date: datetime.date
=======
    time: datetime.date
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    tasks_user: list[TaskUser]


class AddUserTask(BaseModel):
<<<<<<< HEAD
    """Schemas for add user in tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    task_id: int
    user_id: int
    user_role: models.UserTaskRole


class AddUserTaskResponse(AddUserTask):
<<<<<<< HEAD
    """Response schemas for add user in tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    id: int


class TaskResponse(CreateTask):
<<<<<<< HEAD
    """Schemas for get tasks"""

    id: int
    date: datetime.date
=======
    id: int
    time: datetime.date
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    tasks_user: list[TaskUser]


class TaskUpdate(BaseModel):
<<<<<<< HEAD
    """Schemas for update response"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    title: str | None = None
    descriptions: str | None = None


class TaskStatusUpdate(BaseModel):
<<<<<<< HEAD
    """Schemas for update tasks status or comment"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    status: models.TaskStatus | None = None
    comments: str | None = None


class TaskStatusUpdateResponse(BaseModel):
<<<<<<< HEAD
    """Response schemas for update tasks status or comment"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    status: models.TaskStatus
    comments: str
    title: str
    descriptions: str


class CreareGrade(BaseModel):
<<<<<<< HEAD
    """Schemas foor create grade tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    user_id: int
    grade: int


class CreateGradeResponse(CreareGrade):
<<<<<<< HEAD
    """Response schemas foor create grade tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    id: int


class GetGrade(BaseModel):
<<<<<<< HEAD
    """Schemas for get grade woth date filters"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    date_start: datetime.date
    date_end: datetime.date


class MeetingUser(BaseModel):
<<<<<<< HEAD
    """Schemas for meeting for user"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    user_id: int


class CreateMeeting(BaseModel):
<<<<<<< HEAD
    """Schemas for create meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    title: str
    date: datetime.date
    time: datetime.time


class CreateMeetingResponse(CreateMeeting):
<<<<<<< HEAD
    """Response schemas for create meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    id: int
    meeting_user: list[MeetingUser]


class UpdateMeeting(BaseModel):
<<<<<<< HEAD
    """Schemas for update meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    title: str | None = None
    date: datetime.date | None = None
    time: datetime.time | None = None


class AddUserMeeting(BaseModel):
<<<<<<< HEAD
    """Schemas for add user for meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    user_id: int
    meeting_id: int


class AddUserMeetingResponse(AddUserMeeting):
<<<<<<< HEAD
    """Response schemas for add user for meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    meetings: CreateMeeting
