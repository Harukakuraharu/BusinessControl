from typing import Annotated, Optional

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.functional_validators import AfterValidator


def validate_password(password: str) -> str:
<<<<<<< HEAD
    """Validate password"""
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    assert len(password) >= 8, f"{password} is short"
    assert password.isalnum(), f"{password} must contain numbers and letters"
    return password


Password = Annotated[str, AfterValidator(validate_password)]


class Organization(BaseModel):
<<<<<<< HEAD
    """Schemas for organization field on UserResponse schema"""

    role: models.UserRole
    company_id: int
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    """Schemas for user"""

=======
    role: models.UserRole
    compamy_id: int


class User(BaseModel):
>>>>>>> 3f2822f (Complete servis with admin and company)
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(User):
<<<<<<< HEAD
    """Schemas for create user for password"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    password: Password


class UserResponse(User):
<<<<<<< HEAD
    """Response schemas for create user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    id: int
    is_admin: bool
    is_super_admin: bool
    organization: Optional["Organization"]
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
<<<<<<< HEAD
    """Schemas for user token"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    access_token: str


class UserLogin(BaseModel):
<<<<<<< HEAD
    """Schemas for login user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    email: str
    password: str


class UserUpdate(BaseModel):
<<<<<<< HEAD
    """Schemas for update user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    first_name: str | None = None
    last_name: str | None = None


class JoinCompany(BaseModel):
<<<<<<< HEAD
    """Schemas for add user on company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    code: str


class JoinCompanyResponse(BaseModel):
<<<<<<< HEAD
    """Response schemas for add user on company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    company_id: int
    user_id: int
