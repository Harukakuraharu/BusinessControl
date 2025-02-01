from typing import Type, TypeVar

from database.models.base import Base
from database.models.companies import Company, News, Organization, UserRole
from database.models.meetings import Meeting, MeetingUser
from database.models.tasks import (
    Motivation,
    Task,
    TaskStatus,
    TaskUser,
    UserTaskRole,
)
from database.models.users import User


MODEL = TypeVar("MODEL", bound=Base)

TypeModel = Type[MODEL]
