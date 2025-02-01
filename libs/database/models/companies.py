import enum

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.utils import intpk


class UserRole(enum.Enum):
    SUPER_MANAGER = "super_manager"
    MANAGER = "manager"
    EMPLOYEE = "employee"


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[intpk]
    title: Mapped[str]
    organization: Mapped[list["Organization"]] = relationship(
        back_populates="company", lazy="joined"
    )
    news: Mapped[list["News"]] = relationship(
        back_populates="company", lazy="joined"
    )


class Organization(Base):
    __tablename__ = "organization"
    __table_args__ = (UniqueConstraint("company_id", "user_id"),)

    id: Mapped[intpk]
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    role: Mapped[UserRole]
    company: Mapped[Company] = relationship(
        back_populates="organization", lazy="joined"
    )
<<<<<<< HEAD
<<<<<<< HEAD
    user: Mapped["User"] = relationship(  # type: ignore[name-defined]
=======
    user: Mapped["User"] = relationship(
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
    user: Mapped["User"] = relationship(  # type: ignore[name-defined]
>>>>>>> e7f03f9 (Added docs)
        back_populates="organization", lazy="joined"
    )


class News(Base):
    __tablename__ = "news"

    id: Mapped[intpk]
    title: Mapped[str]
    descriptions: Mapped[str]
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE")
    )
    company: Mapped[Company] = relationship(
        back_populates="news", lazy="joined"
    )
