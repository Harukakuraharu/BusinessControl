from typing import Type, TypeVar

from database.models.base import Base
from database.models.users import Company, CompanyEmployeers, User, UserRole


MODEL = TypeVar("MODEL", bound=Base)

TypeModel = Type[MODEL]
