from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CompanyCreate(BaseModel):
    title: str


class CompanyCreateResponse(CompanyCreate):
    id: int


class AdminStatus(BaseModel):
    email: EmailStr


class CompanyEmployeers(BaseModel):
    user_id: int
    role: models.UserRole


class CompanyEmployersResponse(BaseModel):
    id: int
    title: str
    organization: list[CompanyEmployeers]


class AddUserOrganization(BaseModel):
    email: EmailStr
    role: models.UserRole


class CreateNews(BaseModel):
    title: str
    descriptions: str


class CreateNewsResponse(CreateNews):
    id: int
    company_id: int


class UpdateNews(BaseModel):
    title: str | None = None
    descriptions: str | None = None


class CreateCode(BaseModel):
    role: models.UserRole
