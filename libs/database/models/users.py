<<<<<<< HEAD
<<<<<<< HEAD
from sqlalchemy import false
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.utils import intpk
=======
import enum

from sqlalchemy import ForeignKey, false
from sqlalchemy.orm import Mapped, mapped_column
=======
from sqlalchemy import false
from sqlalchemy.orm import Mapped, mapped_column, relationship
>>>>>>> 3f2822f (Complete servis with admin and company)

from database.models.base import Base
from database.models.utils import intpk


<<<<<<< HEAD
class UserRole(enum.Enum):
    SUPER_MANAGER = "super_manager"
    MANAGER = "manager"
    EMPLOYEE = "employee"
>>>>>>> a0a9e11 (Fix folders)


=======
>>>>>>> 3f2822f (Complete servis with admin and company)
class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
<<<<<<< HEAD
<<<<<<< HEAD
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    is_super_admin: Mapped[bool] = mapped_column(server_default=false())
    is_admin: Mapped[bool] = mapped_column(server_default=false())
<<<<<<< HEAD
    organization: Mapped["Organization"] = relationship(  # type: ignore[name-defined]
        back_populates="user", lazy="joined"
    )
    tasks_user: Mapped[list["TaskUser"]] = relationship(  # type: ignore[name-defined]
        back_populates="users", lazy="selectin"
    )
    meeting_user: Mapped[list["MeetingUser"]] = relationship(  # type: ignore[name-defined]
        back_populates="users", lazy="selectin"
    )
    motivations: Mapped[list["Motivation"]] = relationship(  # type: ignore[name-defined]
        back_populates="users", lazy="joined"
    )
=======
    email: Mapped[str]
=======
    email: Mapped[str] = mapped_column(unique=True)
>>>>>>> 09b7086 (Add user routers)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    is_super_admin: Mapped[bool] = mapped_column(server_default=false())
    is_admin: Mapped[bool] = mapped_column(server_default=false())


# create_compamy
# Если is_admin = True, создается компания, и у


class News(Base):
    __tablename__ = "news"

    id: Mapped[intpk]
    title: Mapped[str]
    descriptions: Mapped[str]
    image: Mapped[str]


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[intpk]
    title: Mapped[str]
    news_id: Mapped[int] = mapped_column(
        ForeignKey("news.id", ondelete="CASCADE")
    )


class CompanyEmployeers(Base):
    __tablename__ = "company_employeers"

    id: Mapped[intpk]
    compamy_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    role: Mapped[UserRole]
>>>>>>> a0a9e11 (Fix folders)
=======
    organization: Mapped["Organization"] = relationship(
        back_populates="user", lazy="joined"
    )
<<<<<<< HEAD
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    tasks_user: Mapped[list["TaskUser"]] = relationship(
        back_populates="users", lazy="selectin"
    )
    meeting_user: Mapped[list["MeetingUser"]] = relationship(
        back_populates="users", lazy="selectin"
    )
    motivations: Mapped[list["Motivation"]] = relationship(
        back_populates="users", lazy="joined"
    )   
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
