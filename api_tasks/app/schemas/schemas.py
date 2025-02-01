import datetime

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Main schemas for user"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Main schemas for user"""

>>>>>>> e7f03f9 (Added docs)
    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
<<<<<<< HEAD
<<<<<<< HEAD
    """Main response schemas for user"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Main response schemas for user"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CreateTask(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for create task"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for create task"""

>>>>>>> e7f03f9 (Added docs)
    title: str
    descriptions: str
    status: models.TaskStatus


class TaskUser(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for tasks_user field on CreateTaskResponse schemas"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for tasks_user field on CreateTaskResponse schemas"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    user_id: int
    task_id: int
    user_role: models.UserTaskRole


class CreateTaskResponse(CreateTask):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for create tasks"""

    date: datetime.date
=======
=======
    """Response schemas for create tasks"""

>>>>>>> e7f03f9 (Added docs)
    time: datetime.date
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    tasks_user: list[TaskUser]


class AddUserTask(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for add user in tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for add user in tasks"""

>>>>>>> e7f03f9 (Added docs)
    task_id: int
    user_id: int
    user_role: models.UserTaskRole


class AddUserTaskResponse(AddUserTask):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for add user in tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Response schemas for add user in tasks"""

>>>>>>> e7f03f9 (Added docs)
    id: int


class TaskResponse(CreateTask):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for get tasks"""

    id: int
    date: datetime.date
=======
=======
    """Schemas for get tasks"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    time: datetime.date
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    tasks_user: list[TaskUser]


class TaskUpdate(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for update response"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for update response"""

>>>>>>> e7f03f9 (Added docs)
    title: str | None = None
    descriptions: str | None = None


class TaskStatusUpdate(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for update tasks status or comment"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for update tasks status or comment"""

>>>>>>> e7f03f9 (Added docs)
    status: models.TaskStatus | None = None
    comments: str | None = None


class TaskStatusUpdateResponse(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for update tasks status or comment"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Response schemas for update tasks status or comment"""

>>>>>>> e7f03f9 (Added docs)
    status: models.TaskStatus
    comments: str
    title: str
    descriptions: str


class CreareGrade(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas foor create grade tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas foor create grade tasks"""

>>>>>>> e7f03f9 (Added docs)
    user_id: int
    grade: int


class CreateGradeResponse(CreareGrade):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas foor create grade tasks"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Response schemas foor create grade tasks"""

>>>>>>> e7f03f9 (Added docs)
    id: int


class GetGrade(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for get grade woth date filters"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for get grade woth date filters"""

>>>>>>> e7f03f9 (Added docs)
    date_start: datetime.date
    date_end: datetime.date


class MeetingUser(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for meeting for user"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for meeting for user"""

>>>>>>> e7f03f9 (Added docs)
    user_id: int


class CreateMeeting(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for create meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for create meeting"""

>>>>>>> e7f03f9 (Added docs)
    title: str
    date: datetime.date
    time: datetime.time


class CreateMeetingResponse(CreateMeeting):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for create meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Response schemas for create meeting"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    meeting_user: list[MeetingUser]


class UpdateMeeting(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for update meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for update meeting"""

>>>>>>> e7f03f9 (Added docs)
    title: str | None = None
    date: datetime.date | None = None
    time: datetime.time | None = None


class AddUserMeeting(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for add user for meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Schemas for add user for meeting"""

>>>>>>> e7f03f9 (Added docs)
    user_id: int
    meeting_id: int


class AddUserMeetingResponse(AddUserMeeting):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for add user for meeting"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Response schemas for add user for meeting"""

>>>>>>> e7f03f9 (Added docs)
    meetings: CreateMeeting
