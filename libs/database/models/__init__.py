from typing import Type, TypeVar

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
from database.models.users import User
from database.models.base import Base
from database.models.companies import Company, Organization, UserRole, News
<<<<<<< HEAD
>>>>>>> 3f2822f (Complete servis with admin and company)

=======
from database.models.tasks import Task, TaskStatus, TaskUser, UserTaskRole, Motivation
from database.models.meetings import Meeting, MeetingUser
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
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

>>>>>>> e7f03f9 (Added docs)

MODEL = TypeVar("MODEL", bound=Base)

TypeModel = Type[MODEL]
