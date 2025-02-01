from datetime import timedelta
from typing import AsyncIterator, Type

import pytest
<<<<<<< HEAD
<<<<<<< HEAD
from core.dependency import get_session
from core.settings import config
=======
>>>>>>> 6230ac8 (Added api tests)
=======
from core.dependency import get_session
from core.settings import config
>>>>>>> e7f03f9 (Added docs)
from database import models
from database.models import Base
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
<<<<<<< HEAD
<<<<<<< HEAD
from main import app
=======
>>>>>>> 6230ac8 (Added api tests)
=======
from main import app
>>>>>>> e7f03f9 (Added docs)
from redis_cli.redis_client import redis_client
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from tests_config import factory as fc
from tests_config import utils

<<<<<<< HEAD
<<<<<<< HEAD

@pytest.fixture(scope="session")
def anyio_backend() -> str:
=======
from core.dependency import get_session
from core.settings import config
from main import app


@pytest.fixture(scope="session")
def anyio_backend():
>>>>>>> 6230ac8 (Added api tests)
=======

@pytest.fixture(scope="session")
def anyio_backend() -> str:
>>>>>>> e7f03f9 (Added docs)
    return "asyncio"


@pytest.fixture(scope="session", name="pg_url")
def pg_url_fixture() -> str:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    URL with host localhost for test
=======
    Формирование URL для тестовой БД с localhost
>>>>>>> 6230ac8 (Added api tests)
=======
    URL with host localhost for test
>>>>>>> e7f03f9 (Added docs)
    """
    config.DB_HOST = "localhost"
    return config.async_dsn  # type: ignore[return-value]


@pytest.fixture(scope="session", autouse=True, name="postgres_temlate")
async def postgres_temlate_fixture(pg_url: str) -> AsyncIterator[str]:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    Create tempalate database with migrations for create another database
=======
    Создаем шаблонную БД с миграциями для создания других БД.
    Миграции создаются в run_sync, вызывая metadata.create_all.
    Эта БД создается один раз для всех тестов
>>>>>>> 6230ac8 (Added api tests)
=======
    Create tempalate database with migrations for create another database
>>>>>>> e7f03f9 (Added docs)
    """
    async with utils.async_tmp_database(
        pg_url, db_name="api_template"
    ) as tmp_url:
        engine = utils.create_async_engine(tmp_url)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        await engine.dispose()
        yield tmp_url


@pytest.fixture(name="postgres")
async def postgres_fixture(postgres_temlate: str) -> AsyncIterator[str]:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    With template for database in previous fixture
    create test database with all migrations for tests
=======
    На основе шаблона БД из предыдущей фикстуры, создается тестовая БД,
    где уже есть все миграции
>>>>>>> 6230ac8 (Added api tests)
=======
    With template for database in previous fixture
    create test database with all migrations for tests
>>>>>>> e7f03f9 (Added docs)
    """
    async with utils.async_tmp_database(
        postgres_temlate, db_name="temp_db", template="api_template"
    ) as tmp_url:
        yield tmp_url


@pytest.fixture(name="postgres_engine")
async def postgres_engine_fixture(postgres: str) -> AsyncIterator[AsyncEngine]:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    Create engine for test database
=======
    Фикстура для создания engine
>>>>>>> 6230ac8 (Added api tests)
=======
    Create engine for test database
>>>>>>> e7f03f9 (Added docs)
    """
    engine = utils.create_async_engine(postgres)  # type: ignore
    try:
        yield engine
    finally:
        await engine.dispose()


@pytest.fixture(name="async_session")
async def async_session_fixture(
    postgres_engine: AsyncEngine,
) -> AsyncIterator[AsyncSession]:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    Create async session
=======
    Создание сессии с подключением к тестовой БД
>>>>>>> 6230ac8 (Added api tests)
=======
    Create async session
>>>>>>> e7f03f9 (Added docs)
    """
    async with AsyncSession(postgres_engine) as session:
        yield session


@pytest.fixture(name="test_app")
async def test_app_fixture(
    async_session: AsyncSession,
) -> AsyncIterator[FastAPI]:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    Dependency replacementeplacement main config for test
=======
    Подмена зависимостей основого приложение на тестовые
>>>>>>> 6230ac8 (Added api tests)
=======
    Dependency replacementeplacement main config for test
>>>>>>> e7f03f9 (Added docs)
    """
    app.dependency_overrides[get_session] = lambda: async_session
    yield app
    app.dependency_overrides = {}


@pytest.fixture(name="client")
async def client_fixture(test_app: FastAPI) -> AsyncIterator[AsyncClient]:
    """
<<<<<<< HEAD
<<<<<<< HEAD
    Create client for execution requests without auth
=======
    Создание клиента для отправки запросов без авторизации
>>>>>>> 6230ac8 (Added api tests)
=======
    Create client for execution requests without auth
>>>>>>> e7f03f9 (Added docs)
    """
    async with AsyncClient(
        transport=ASGITransport(app=test_app), base_url="http://test"
    ) as async_client:
        yield async_client


@pytest.fixture(name="factory")
async def factory_fixture(async_session: AsyncSession):
<<<<<<< HEAD
<<<<<<< HEAD
    """Fixture for factory"""

=======
>>>>>>> 6230ac8 (Added api tests)
=======
    """Fixture for factory"""

>>>>>>> e7f03f9 (Added docs)
    async def wrapper(cls: Type[fc.MainFactory], count=1, **kwargs):
        result = await cls(async_session).generate_data(count, **kwargs)
        if len(result) == 1:
            return result[0]
        return result

    return wrapper


@pytest.fixture(name="user_client")
async def user_client_fixture(
    factory, test_app: FastAPI
) -> AsyncIterator[AsyncClient]:
<<<<<<< HEAD
<<<<<<< HEAD
    """Create client for execution requests with auth"""
=======
>>>>>>> 6230ac8 (Added api tests)
=======
    """Create client for execution requests with auth"""
>>>>>>> e7f03f9 (Added docs)
    password = "string123"
    user = await factory(
        fc.UserFactory,
        password=utils.hash_password(password),
        first_name="Test_user",
    )
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token = utils.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )
    async with AsyncClient(
        transport=ASGITransport(app=test_app),
        base_url="http://test",
        headers={"Authorization": f"Bearer {token}"},
    ) as async_client:
        yield async_client


@pytest.fixture(name="admin_client")
async def admin_client_fixture(
    factory, test_app: FastAPI
) -> AsyncIterator[AsyncClient]:
<<<<<<< HEAD
<<<<<<< HEAD
    """Create admin client for execution requests
    with auth anf flag is_admin"""
=======
>>>>>>> 6230ac8 (Added api tests)
=======
    """Create admin client for execution requests
    with auth anf flag is_admin"""
>>>>>>> e7f03f9 (Added docs)
    password = "string123"
    user = await factory(
        fc.UserFactory,
        password=utils.hash_password(password),
        first_name="Test_user",
        is_admin=True,
    )
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token = utils.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )
    async with AsyncClient(
        transport=ASGITransport(app=test_app),
        base_url="http://test",
        headers={"Authorization": f"Bearer {token}"},
    ) as async_client:
        yield async_client


@pytest.fixture(name="admin_company_client")
async def admin_company_client_fixture(
    factory, test_app: FastAPI
) -> AsyncIterator[AsyncClient]:
<<<<<<< HEAD
<<<<<<< HEAD
    """Create admin client for execution requests
    with auth and company"""
=======
>>>>>>> 6230ac8 (Added api tests)
=======
    """Create admin client for execution requests
    with auth and company"""
>>>>>>> e7f03f9 (Added docs)
    await factory(fc.CompanyFactory)
    password = "string123"
    user = await factory(
        fc.UserFactory,
        password=utils.hash_password(password),
        first_name="Test_admin",
        is_admin=True,
    )
    await factory(fc.OrganizationFactory, user_id=user.id)
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token = utils.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )
    async with AsyncClient(
        transport=ASGITransport(app=test_app),
        base_url="http://test",
        headers={"Authorization": f"Bearer {token}"},
    ) as async_client:
        yield async_client


@pytest.fixture(name="user_company_client")
async def user_company_client_fixture(
    factory, test_app: FastAPI
) -> AsyncIterator[AsyncClient]:
<<<<<<< HEAD
<<<<<<< HEAD
    """Create user client for execution requests
    with auth and company"""
=======
>>>>>>> 6230ac8 (Added api tests)
=======
    """Create user client for execution requests
    with auth and company"""
>>>>>>> e7f03f9 (Added docs)
    await factory(fc.CompanyFactory)
    password = "string123"
    user = await factory(
        fc.UserFactory,
        password=utils.hash_password(password),
        first_name="Test_user",
    )
    await factory(
        fc.OrganizationFactory, user_id=user.id, role=models.UserRole.EMPLOYEE
    )
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token = utils.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )
    async with AsyncClient(
        transport=ASGITransport(app=test_app),
        base_url="http://test",
        headers={"Authorization": f"Bearer {token}"},
    ) as async_client:
        yield async_client


@pytest.fixture(name="clear_redis", autouse=True)
async def clear_redis_fixture():
<<<<<<< HEAD
<<<<<<< HEAD
    """Clean redis with code"""
=======
>>>>>>> 6230ac8 (Added api tests)
=======
    """Clean redis with code"""
>>>>>>> e7f03f9 (Added docs)
    yield
    if redis_client.keys():
        redis_client.delete(*redis_client.keys())
