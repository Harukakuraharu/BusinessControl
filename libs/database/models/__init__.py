from typing import Type, TypeVar

from database.models.users import User
from database.models.base import Base
from database.models.companies import Company, Organization, UserRole, News


MODEL = TypeVar("MODEL", bound=Base)

TypeModel = Type[MODEL]
