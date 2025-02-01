from database import models
from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Main schemas for user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Main schemas for user"""

>>>>>>> e7f03f9 (Added docs)
    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(User):
<<<<<<< HEAD
<<<<<<< HEAD
    """Main response schemas for user"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Main response schemas for user"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    is_admin: bool
    is_super_admin: bool
    model_config = ConfigDict(from_attributes=True)


class CompanyCreate(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for create company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for create company"""

>>>>>>> e7f03f9 (Added docs)
    title: str


class CompanyCreateResponse(CompanyCreate):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for create company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Response schemas for create company"""

>>>>>>> e7f03f9 (Added docs)
    id: int


class AdminStatus(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for update user status on admin"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for update user status on admin"""

>>>>>>> e7f03f9 (Added docs)
    email: EmailStr


class CompanyEmployeers(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for add user in company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Response schemas for add user in company"""

>>>>>>> e7f03f9 (Added docs)
    user_id: int
    role: models.UserRole


class CompanyEmployersResponse(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for get company with employee"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Response schemas for get company with employee"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    title: str
    organization: list[CompanyEmployeers]


class AddUserOrganization(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for add user in company"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for add user in company"""

>>>>>>> e7f03f9 (Added docs)
    email: EmailStr
    role: models.UserRole


class CreateNews(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for create news"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for create news"""

>>>>>>> e7f03f9 (Added docs)
    title: str
    descriptions: str


class CreateNewsResponse(CreateNews):
<<<<<<< HEAD
<<<<<<< HEAD
    """Response schemas for create news"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Response schemas for create news"""

>>>>>>> e7f03f9 (Added docs)
    id: int
    company_id: int


class UpdateNews(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for update news"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for update news"""

>>>>>>> e7f03f9 (Added docs)
    title: str | None = None
    descriptions: str | None = None


class CreateCode(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """Schemas for create code"""

=======
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    """Schemas for create code"""

>>>>>>> e7f03f9 (Added docs)
    role: models.UserRole
