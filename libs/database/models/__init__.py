from typing import Type, TypeVar

from database.models.users import User
from database.models.base import Base
from database.models.companies import Company, Organization, UserRole, News
from database.models.tasks import Task, TaskStatus, TaskUser, UserTaskRole, Motivation
from database.models.meetings import Meeting, MeetingUser

MODEL = TypeVar("MODEL", bound=Base)

TypeModel = Type[MODEL]
