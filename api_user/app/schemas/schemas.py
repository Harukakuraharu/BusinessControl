from typing import Annotated, Optional

from database import models
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.functional_validators import AfterValidator


def validate_password(password: str) -> str:
    assert len(password) >= 8, f"{password} is short"
    assert password.isalnum(), f"{password} must contain numbers and letters"
    return password


Password = Annotated[str, AfterValidator(validate_password)]


class Organization(BaseModel):
    role: models.UserRole
    compamy_id: int


class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(User):
    password: Password


class UserResponse(User):
    id: int
    is_admin: bool
    is_super_admin: bool
    organization: Optional["Organization"]
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None


class JoinCompany(BaseModel):
    code: str


class JoinCompanyResponse(BaseModel):
    company_id: int
    user_id: int
