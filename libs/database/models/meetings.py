import datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.utils import intpk


class Meeting(Base):
    __tablename__ = "meetings"

    id: Mapped[intpk]
    title: Mapped[str]
    date: Mapped[datetime.date]
    time: Mapped[datetime.time]
    meeting_user: Mapped[list["MeetingUser"]] = relationship(
        back_populates="meetings", lazy="selectin"
    )


class MeetingUser(Base):
    __tablename__ = "meeting_user"
    __table_args__ = (UniqueConstraint("meeting_id", "user_id"),)
    
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    meeting_id: Mapped[int] = mapped_column(
        ForeignKey("meetings.id", ondelete="CASCADE")
    )
    users: Mapped["User"] = relationship(
        back_populates="meeting_user", lazy="joined"
    )
    meetings: Mapped[Meeting] = relationship(
        back_populates="meeting_user", lazy="joined"
    )
