import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.utils import intpk


class UserRole(enum.Enum):
    SUPER_MANAGER = "super_manager"
    MANAGER = "manager"
    EMPLOYEE = "employee"


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str]
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    is_super_admin: Mapped[bool]
    is_admin: Mapped[bool]


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
