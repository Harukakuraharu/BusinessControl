import datetime

<<<<<<< HEAD
import sqlalchemy as sa
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.utils import intpk


class Meeting(Base):
    __tablename__ = "meetings"

    id: Mapped[intpk]
    title: Mapped[str]
    date: Mapped[datetime.date]
<<<<<<< HEAD
    time: Mapped[datetime.time] = mapped_column(sa.Time(timezone=False))
=======
    time: Mapped[datetime.time]
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    meeting_user: Mapped[list["MeetingUser"]] = relationship(
        back_populates="meetings", lazy="selectin"
    )


class MeetingUser(Base):
    __tablename__ = "meeting_user"
    __table_args__ = (UniqueConstraint("meeting_id", "user_id"),)
<<<<<<< HEAD

=======
    
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    meeting_id: Mapped[int] = mapped_column(
        ForeignKey("meetings.id", ondelete="CASCADE")
    )
<<<<<<< HEAD
    users: Mapped["User"] = relationship(  # type: ignore[name-defined]
=======
    users: Mapped["User"] = relationship(
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
        back_populates="meeting_user", lazy="joined"
    )
    meetings: Mapped[Meeting] = relationship(
        back_populates="meeting_user", lazy="joined"
    )
