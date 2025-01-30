<<<<<<< HEAD
from core import dependency
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import schemas
from services.services_meetings import MeetingServices

=======
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from services.services_meetings import MeetingServices

from core import dependency
from schemas import schemas


>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
meetings_routers = APIRouter(prefix="/meetings", tags=["Meetings"])


@meetings_routers.post("/", response_model=schemas.CreateMeetingResponse)
async def create_meetings(
    session: dependency.AsyncSessionDependency,
    data: schemas.CreateMeeting,
    user: dependency.GetCurrentUserDependency,
):
<<<<<<< HEAD
    """Create meeting"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    return await MeetingServices(session).create_meeting(data, user.id)


@meetings_routers.get("/", response_model=list[schemas.CreateMeetingResponse])
async def get_meetings(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
):
<<<<<<< HEAD
    """Get owner meetings"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    return await MeetingServices(session).get_meeting(user.id)


@meetings_routers.patch(
    "/{meeting_id}/", response_model=schemas.CreateMeetingResponse
)
async def update_meetings(
    session: dependency.AsyncSessionDependency,
    data: schemas.UpdateMeeting,
    user: dependency.GetCurrentUserDependency,
    meeting_id: int,
):
<<<<<<< HEAD
    """Update meeting"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    return await MeetingServices(session).update_meeting(
        user.id, data, meeting_id
    )


@meetings_routers.delete("/{meeting_id}/")
async def delete_meeting(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
    meeting_id: int,
):
<<<<<<< HEAD
    """Delete meeting"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    await MeetingServices(session).delete_meeting(user.id, meeting_id)
    return JSONResponse(
        content="Successfully deleted", status_code=status.HTTP_200_OK
    )


@meetings_routers.post(
    "/add_user/", response_model=schemas.AddUserMeetingResponse
)
async def add_user_meeting(
    session: dependency.AsyncSessionDependency,
    user: dependency.GetCurrentUserDependency,
    data: schemas.AddUserMeeting,
):
<<<<<<< HEAD
    """Add user in meeting"""
=======
>>>>>>> 0c00bcb (Complete servis with tasks and meetings)
    return await MeetingServices(session).add_user_meeting(data, user.id)
