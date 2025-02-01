from sqlalchemy import false
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.utils import intpk


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    is_super_admin: Mapped[bool] = mapped_column(server_default=false())
    is_admin: Mapped[bool] = mapped_column(server_default=false())
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
