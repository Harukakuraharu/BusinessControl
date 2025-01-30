import json

import pytest
from fastapi import status
from httpx import AsyncClient
from redis_cli.redis_client import redis_client
from tests_config import factory as fc


pytestmark = pytest.mark.anyio


@pytest.mark.parametrize(
    "password, status_code",
    [
        ("qwerty123", status.HTTP_200_OK),
        ("qwerty", status.HTTP_422_UNPROCESSABLE_ENTITY),
        ("q123", status.HTTP_422_UNPROCESSABLE_ENTITY),
    ],
)
async def test_create_user(
    client: AsyncClient, password: str, status_code: status
):
    """Test create user with different password"""
    data = {
        "first_name": "Hello",
        "last_name": "World",
        "email": "qwerty@mail.ru",
        "password": password,
    }
    response = await client.post("/user/registration/", json=data)
    assert response.status_code == status_code
    if status_code == status.HTTP_200_OK:
        data.pop("password")
        response.json().pop("id")
        assert all(
            response.json()[key] == data[key]
            for key in data  # pylint: disable=C0206
        )
        assert "password" not in response.json()


async def test_auth_user(client: AsyncClient, factory):
    """Auth user"""
    password = "string123"
    user = await factory(fc.UserFactory, password=password)
    data = {
        "email": user.email,
        "password": password,
    }
    response = await client.post("/user/auth/", json=data)
    assert response.status_code == status.HTTP_200_OK


async def test_auth_user_with_invalid_password(client: AsyncClient, factory):
    """Auth with incorrect password"""
    password = "string123"
    user = await factory(fc.UserFactory, password=password)
    data = {
        "email": user.email,
        "password": "string12345",
    }
    response = await client.post("/user/auth/", json=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_get_user(user_client: AsyncClient):
    """Get info about youself"""
    response = await user_client.get("user/me/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["first_name"] == "Test_user"


async def test_get_user_id(client: AsyncClient):
    """Get info about youself without auth"""
    response = await client.get("user/me/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_update_info(user_client: AsyncClient):
    """Update info field about youself"""
    update_data = {"first_name": "Hehehe"}
    response = await user_client.patch("/user/me/", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("first_name") == update_data["first_name"]


async def test_delete_current_user(user_client: AsyncClient):
    """Delete youself"""
    response = await user_client.delete("/user/me/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize(
    "code, status_code",
    [
        ("qwerty1234", status.HTTP_200_OK),
        ("zxcvbnm1234", status.HTTP_400_BAD_REQUEST),
    ],
)
async def test_join_company(
    user_client: AsyncClient, factory, code, status_code
):
    """Join company with correct and incorrect code"""
    company = await factory(fc.CompanyFactory)
    set_data = {"company_id": company.id, "role": "manager"}
    redis_client.set("qwerty1234", json.dumps(set_data))
    response = await user_client.post(
        "/user/join_company/", json={"code": code}
    )
    assert response.status_code == status_code
