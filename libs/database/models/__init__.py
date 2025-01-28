from typing import Type, TypeVar

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
from models.base import Base
from models.users import Company, CompanyEmployeers, User, UserRole
>>>>>>> a0a9e11 (Fix folders)
=======
from database.models.base import Base
from database.models.users import Company, CompanyEmployeers, User, UserRole
>>>>>>> 09b7086 (Add user routers)


MODEL = TypeVar("MODEL", bound=Base)

TypeModel = Type[MODEL]
