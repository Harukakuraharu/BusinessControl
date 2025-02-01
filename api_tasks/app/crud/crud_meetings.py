import sqlalchemy as sa
from database import models
from fastapi import HTTPException, status
from repository.base_crud import BaseCrud


class MeetingCrud(BaseCrud):
<<<<<<< HEAD
<<<<<<< HEAD
    """Execution of the request in database for meeting model"""

=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    """Execution of the request in database for meeting model"""

>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.Meeting

<<<<<<< HEAD
<<<<<<< HEAD
    async def get_meetings(self, user_id: int) -> list:
        """Get all meeting for current user"""
=======
    async def get_meetings(self, user_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
    async def get_meetings(self, user_id: int) -> list:
        """Get all meeting for current user"""
>>>>>>> e7f03f9 (Added docs)
        stmt = sa.select(self.model).where(
            self.model.meeting_user.any(user_id=user_id)
        )
        response = await self.session.scalars(stmt)
        return response.unique().all()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e7f03f9 (Added docs)
    async def get_meeting(
        self, user_id: int, meeting_id: int
    ) -> models.Meeting:
        """Get meeting by id"""
<<<<<<< HEAD
=======
    async def get_meeting(self, user_id: int, meeting_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
>>>>>>> e7f03f9 (Added docs)
        stmt = (
            sa.select(self.model)
            .join(
                models.MeetingUser,
                models.MeetingUser.meeting_id == self.model.id,
            )
            .where(
                models.MeetingUser.user_id == user_id,
                self.model.id == meeting_id,
            )
        )
        result = await self.session.execute(stmt)
<<<<<<< HEAD
<<<<<<< HEAD
        meeting = result.scalars().all()
        if len(meeting) == 0:
=======
        task = result.scalars().all()
        if len(task) == 0:
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
        meeting = result.scalars().all()
        if len(meeting) == 0:
>>>>>>> e7f03f9 (Added docs)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You have not a permission to perform this action",
            )
<<<<<<< HEAD
<<<<<<< HEAD
        return meeting


class MeetingUserCrud(BaseCrud):
    """Execution of the request in database for meeting-user model"""
=======
        return task


class MeetingUserCrud(BaseCrud):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
=======
        return meeting


class MeetingUserCrud(BaseCrud):
    """Execution of the request in database for meeting-user model"""
>>>>>>> e7f03f9 (Added docs)
    def __init__(self, session):
        super().__init__(session)
        self.model = models.MeetingUser
