from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    """Main schemas for user"""

    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
    """Main response schemas for user"""

    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CompanyCreate(BaseModel):
    """Schemas for create company"""

    title: str


class CompanyCreateResponse(CompanyCreate):
    """Response schemas for create company"""

    id: int


class AdminStatus(BaseModel):
    """Schemas for update user status on admin"""

    email: EmailStr


class CompanyEmployeers(BaseModel):
    """Response schemas for add user in company"""

    user_id: int
    role: models.UserRole


class CompanyEmployersResponse(BaseModel):
    """Response schemas for get company with employee"""

    id: int
    title: str
    organization: list[CompanyEmployeers]


class AddUserOrganization(BaseModel):
    """Schemas for add user in company"""

    email: EmailStr
    role: models.UserRole


class CreateNews(BaseModel):
    """Schemas for create news"""

    title: str
    descriptions: str


class CreateNewsResponse(CreateNews):
    """Response schemas for create news"""

    id: int
    company_id: int


class UpdateNews(BaseModel):
    """Schemas for update news"""

    title: str | None = None
    descriptions: str | None = None


class CreateCode(BaseModel):
    """Schemas for create code"""

    role: models.UserRole
