import datetime
import enum

from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.utils import intpk


class TaskStatus(enum.Enum):
    IN_PROGRES = "in_progres"
    NEW = "new"
    DONE = "done"
    UPDATE = "update"


class UserTaskRole(enum.Enum):
    WORKER = "worker"
    AUTHOR = "author"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    title: Mapped[str]
    descriptions: Mapped[str]
    status: Mapped[TaskStatus]
    comments: Mapped[str] = mapped_column(nullable=True)
    time: Mapped[datetime.date] = mapped_column(server_default=func.now())
    tasks_user: Mapped[list["TaskUser"]] = relationship(
        back_populates="tasks", lazy="selectin"
    )
    motivations: Mapped[list["Motivation"]] = relationship(
        back_populates="tasks", lazy="selectin"
    )


class TaskUser(Base):
    __tablename__ = "taskuser"
    __table_args__ = (UniqueConstraint("task_id", "user_id"),)

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE")
    )
    user_role: Mapped[UserTaskRole]
    tasks: Mapped[Task] = relationship(
        back_populates="tasks_user", lazy="joined"
    )
    users: Mapped["User"] = relationship(
        back_populates="tasks_user", lazy="joined"
    )


class Motivation(Base):
    __tablename__ = "motivations"
    __table_args__ = (
        CheckConstraint("grade > 0", name="grade_gt_0"),
        UniqueConstraint("task_id", "user_id"),
    )

    id: Mapped[intpk]
    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    grade: Mapped[int]
    users: Mapped["User"] = relationship(
        back_populates="motivations", lazy="joined"
    )
    tasks: Mapped[Task] = relationship(
        back_populates="motivations", lazy="joined"
    )
