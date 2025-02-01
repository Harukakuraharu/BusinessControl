from typing import Annotated, Optional

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.functional_validators import AfterValidator


def validate_password(password: str) -> str:
<<<<<<< HEAD
<<<<<<< HEAD
    """Validate password"""
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Validate password"""
>>>>>>> e7f03f9 (Added docs)
    assert len(password) >= 8, f"{password} is short"
    assert password.isalnum(), f"{password} must contain numbers and letters"
    return password


Password = Annotated[str, AfterValidator(validate_password)]


class Organization(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e7f03f9 (Added docs)
    """Schemas for organization field on UserResponse schema"""

    role: models.UserRole
    company_id: int
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    """Schemas for user"""

<<<<<<< HEAD
=======
    role: models.UserRole
    company_id: int
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
>>>>>>> e7f03f9 (Added docs)
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(User):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for create user for password"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for create user for password"""

>>>>>>> e7f03f9 (Added docs)
    password: Password


class UserResponse(User):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for create user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Response schemas for create user"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    is_admin: bool
    is_super_admin: bool
    organization: Optional["Organization"]
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for user token"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for user token"""

>>>>>>> e7f03f9 (Added docs)
    access_token: str


class UserLogin(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for login user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for login user"""

>>>>>>> e7f03f9 (Added docs)
    email: str
    password: str


class UserUpdate(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for update user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for update user"""

>>>>>>> e7f03f9 (Added docs)
    first_name: str | None = None
    last_name: str | None = None


class JoinCompany(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for add user on company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for add user on company"""

>>>>>>> e7f03f9 (Added docs)
    code: str


class JoinCompanyResponse(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for add user on company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Response schemas for add user on company"""

>>>>>>> e7f03f9 (Added docs)
    company_id: int
    user_id: int
