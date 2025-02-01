from typing import Annotated, Optional

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.functional_validators import AfterValidator


def validate_password(password: str) -> str:
    """Validate password"""
    assert len(password) >= 8, f"{password} is short"
    assert password.isalnum(), f"{password} must contain numbers and letters"
    return password


Password = Annotated[str, AfterValidator(validate_password)]


class Organization(BaseModel):
    """Schemas for organization field on UserResponse schema"""

    role: models.UserRole
    company_id: int
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    """Schemas for user"""

    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(User):
    """Schemas for create user for password"""

    password: Password


class UserResponse(User):
    """Response schemas for create user"""

    id: int
    is_admin: bool
    is_super_admin: bool
    organization: Optional["Organization"]
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    """Schemas for user token"""

    access_token: str


class UserLogin(BaseModel):
    """Schemas for login user"""

    email: str
    password: str


class UserUpdate(BaseModel):
    """Schemas for update user"""

    first_name: str | None = None
    last_name: str | None = None


class JoinCompany(BaseModel):
    """Schemas for add user on company"""

    code: str


class JoinCompanyResponse(BaseModel):
    """Response schemas for add user on company"""

    company_id: int
    user_id: int
