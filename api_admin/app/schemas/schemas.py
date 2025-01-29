from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
<<<<<<< HEAD
    """Main schemas for user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
<<<<<<< HEAD
    """Main response schemas for user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CompanyCreate(BaseModel):
<<<<<<< HEAD
    """Schemas for create company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    title: str


class CompanyCreateResponse(CompanyCreate):
<<<<<<< HEAD
    """Response schemas for create company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    id: int


class AdminStatus(BaseModel):
<<<<<<< HEAD
    """Schemas for update user status on admin"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    email: EmailStr


class CompanyEmployeers(BaseModel):
<<<<<<< HEAD
    """Response schemas for add user in company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    user_id: int
    role: models.UserRole


class CompanyEmployersResponse(BaseModel):
<<<<<<< HEAD
    """Response schemas for get company with employee"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    id: int
    title: str
    organization: list[CompanyEmployeers]


class AddUserOrganization(BaseModel):
<<<<<<< HEAD
    """Schemas for add user in company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    email: EmailStr
    role: models.UserRole


class CreateNews(BaseModel):
<<<<<<< HEAD
    """Schemas for create news"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    title: str
    descriptions: str


class CreateNewsResponse(CreateNews):
<<<<<<< HEAD
    """Response schemas for create news"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    id: int
    company_id: int


class UpdateNews(BaseModel):
<<<<<<< HEAD
    """Schemas for update news"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    title: str | None = None
    descriptions: str | None = None


class CreateCode(BaseModel):
<<<<<<< HEAD
    """Schemas for create code"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    role: models.UserRole
