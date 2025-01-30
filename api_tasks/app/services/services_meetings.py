<<<<<<< HEAD
from database import models
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from crud import crud_meetings as crud
<<<<<<< HEAD
from schemas import schemas


class MeetingServices:
    """Execution of the request for meetng endpoint"""

=======


class MeetingServices:
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud_meeting = crud.MeetingCrud(self.session)
        self.crud_user_meeting = crud.MeetingUserCrud(self.session)

<<<<<<< HEAD
    async def create_meeting(
        self, data: schemas.CreateMeeting, user_id: int
    ) -> models.Meeting:
        """Execution of the request for create meeting"""
=======
    async def create_meeting(self, data, user_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
        meeting = await self.crud_meeting.create_item(data.model_dump())
        meeting_user_data = {
            "user_id": user_id,
            "meeting_id": meeting.id,
        }
        await self.crud_user_meeting.create_item(meeting_user_data)
        await self.session.commit()
        await self.session.refresh(meeting)
        return meeting

<<<<<<< HEAD
    async def get_meeting(self, user_id: int) -> list:
        """Execution of the request for get meeting"""
        meetings = await self.crud_meeting.get_meetings(user_id)
        return meetings

    async def update_meeting(
        self, user_id: int, update_data: schemas.UpdateMeeting, meeting_id: int
    ) -> models.Meeting:
        """Execution of the request for update meeting"""
=======
    async def get_meeting(self, user_id: int):
        meetings = await self.crud_meeting.get_meetings(user_id)
        return meetings

    async def update_meeting(self, user_id: int, update_data, meeting_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
        await self.crud_meeting.get_meeting(user_id, meeting_id)
        data = update_data.model_dump(exclude_unset=True)
        data["id"] = meeting_id
        meeting = await self.crud_meeting.update_item(data)
        await self.session.commit()
        await self.session.refresh(meeting)
        return meeting

<<<<<<< HEAD
    async def delete_meeting(self, user_id: int, meeting_id: int) -> None:
        """Execution of the request for delete meeting"""
=======
    async def delete_meeting(self, user_id: int, meeting_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
        await self.crud_meeting.get_meeting(user_id, meeting_id)
        await self.crud_meeting.delete_item(meeting_id)
        await self.session.commit()

<<<<<<< HEAD
    async def add_user_meeting(
        self, data: schemas.AddUserMeeting, user_id: int
    ) -> models.MeetingUser:
        """Execution of the request for add user for meeting"""
=======
    async def add_user_meeting(self, data, user_id: int):
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
        await self.crud_meeting.get_meeting(user_id, data.meeting_id)
        meeting_user_data = {
            "meeting_id": data.meeting_id,
            "user_id": data.user_id,
        }
        try:
            meeting_user = await self.crud_user_meeting.create_item(
                meeting_user_data
            )
            await self.session.commit()
        except IntegrityError as error:
            if error.orig is not None and "uq_" in error.orig.args[0]:
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    "User already exists in this meeting",
                ) from error
            raise error
        await self.session.refresh(meeting_user)
        return meeting_user
