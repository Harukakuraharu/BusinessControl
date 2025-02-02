import pytest
from fastapi import status
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from tests_config import factory as fc


pytestmark = pytest.mark.anyio


async def test_create_meet_manager(user_client: AsyncClient):
    """Create meet"""
    data = {
        "title": "Hello",
        "date": "2025-01-05",
        "time": "10:00"
    }
    response = await user_client.post("/meetings/", json=data)
    assert response.status_code == status.HTTP_200_OK


async def test_get_all_meet(user_client: AsyncClient, factory):
    """Test get all meet"""
    await factory(fc.MeetingFactory, user_id=1)
    await factory(fc.MeetingUserFactory, user_id=1, meet_id=1)
    response = await user_client.get("/meetings/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


async def test_update_meet(user_client: AsyncClient, factory):
    """Test update meet"""
    data = {"title": "Hello"}
    meet = await factory(fc.MeetingFactory, user_id=1)
    await factory(fc.MeetingUserFactory, user_id=1, meet_id=1)
    response = await user_client.patch(f"/meetings/{meet.id}/", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == data["title"]


async def test_delete_meet(user_client: AsyncClient, factory):
    """Test delete meet"""
    meet = await factory(fc.MeetingFactory, user_id=1)
    await factory(fc.MeetingUserFactory, user_id=1, meet_id=1)
    response = await user_client.delete(f"/meetings/{meet.id}/")
    assert response.status_code == status.HTTP_200_OK


async def test_add_user_meet(
    user_client: AsyncClient, factory, async_session: AsyncSession
):
    """Test add user on meet"""
    meet = await factory(fc.MeetingFactory, user_id=1)
    user = await factory(fc.UserFactory)
    await factory(fc.MeetingUserFactory, user_id=1, meet_id=1)
    await async_session.refresh(user[0])
    data = {"user_id": user[0].id, "meeting_id": meet.id}
    response = await user_client.post("/meetings/add_user/", json=data)
    assert response.status_code == status.HTTP_200_OK
