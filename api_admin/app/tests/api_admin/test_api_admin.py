import pytest
from fastapi import status
from httpx import AsyncClient
from tests_config import factory as fc


pytestmark = pytest.mark.anyio


async def test_create_code_not_admin(user_client: AsyncClient):
    """Create code for join at company by not admin"""
    data = {"role": "manager"}
    response = await user_client.post("/admin/code/", json=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_create_code(admin_company_client: AsyncClient):
    """Create code for join at company"""
    data = {"role": "manager"}
    response = await admin_company_client.post("/admin/code/", json=data)
    assert response.status_code == status.HTTP_200_OK


async def test_create_admin(super_admin_client: AsyncClient, factory):
    """Change user status on admin for create company and organization"""
    user = await factory(fc.UserFactory)
<<<<<<< HEAD
<<<<<<< HEAD
    assert user[1].is_admin == False  # pylint: disable=C0121
=======
    assert user[1].is_admin == False
>>>>>>> 6230ac8 (Added api tests)
=======
    assert user[1].is_admin == False  # pylint: disable=C0121
>>>>>>> e7f03f9 (Added docs)
    response = await super_admin_client.patch(
        "/super_admin/create_admin/", json={"email": user[1].email}
    )
    assert response.status_code == status.HTTP_200_OK


async def test_create_company(admin_client: AsyncClient):
    """Test create company by admin"""
    data = {
        "title": "Hello",
    }
    response = await admin_client.post("/company/", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == data["title"]
    assert all(
        response.json()[key] == data[key]
        for key in data  # pylint: disable=C0206
    )


async def test_create_company_not_admin(user_client: AsyncClient):
    """Test create company by not admin"""
    data = {
        "title": "Hello",
    }
    response = await user_client.post("/company/", json=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_get_user_company(admin_company_client: AsyncClient):
    """Get current user(admin) company"""
    response = await admin_company_client.get("/company/my/")
    assert response.status_code == status.HTTP_200_OK


async def test_update_user_company(admin_company_client: AsyncClient):
    """Update current user(admin) company"""
    response = await admin_company_client.get("/company/my/")
    old_title = response.json()["title"]
    response = await admin_company_client.patch(
        "/company/my/", json={"title": "Mehehe"}
    )
    assert response.status_code == status.HTTP_200_OK
    new_title = response.json()["title"]
    assert old_title != new_title


async def test_delete_user_company(admin_company_client: AsyncClient):
    """Delete current user(admin) company"""
    response = await admin_company_client.delete("/company/my/")
    assert response.status_code == status.HTTP_200_OK


async def test_add_user_yours_company(
    admin_company_client: AsyncClient, factory
):
    """Add user in current user(admin) company"""
    user = await factory(fc.UserFactory)
    data = {
        "email": user[1].email,
        "role": "employee",
    }
    response = await admin_company_client.post("/admin/user/", json=data)
    assert response.status_code == status.HTTP_200_OK
    response = await admin_company_client.post("/admin/user/", json=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


async def test_create_news(admin_company_client: AsyncClient):
    """Create news by current user(admin) company"""
    data = {"title": "Hehehe", "descriptions": "Hohohohho", "company_id": 1}
    response = await admin_company_client.post("/admin/news/", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert all(
        response.json()[key] == data[key]
        for key in data  # pylint: disable=C0206
    )


async def test_get_news(admin_company_client: AsyncClient, factory):
    """Get news of company"""
    count = 5
    await factory(fc.NewsFactory, count)
    response = await admin_company_client.get("/admin/news/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == count


async def test_get_news_id(admin_company_client: AsyncClient, factory):
    """Get news by id of company"""
    news = await factory(fc.NewsFactory)
    response = await admin_company_client.get(f"/admin/news/{news.id}")
    assert response.status_code == status.HTTP_200_OK
    assert news.id == response.json()["id"]


async def test_update_news_id(admin_company_client: AsyncClient, factory):
    """Update news by id of company"""
    news = await factory(fc.NewsFactory)
    data = {"title": "Mehehe"}
    response = await admin_company_client.patch(
        f"/admin/news/{news.id}", json=data
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == data["title"]


async def test_delete_news_id(admin_company_client: AsyncClient, factory):
    """Delete news by id of company"""
    news = await factory(fc.NewsFactory)
    response = await admin_company_client.delete(f"/admin/news/{news.id}")
    assert response.status_code == status.HTTP_200_OK
