from typing import Iterator

import pytest
from alembic.config import Config
<<<<<<< HEAD
from database.core.settings import config
from database.tests.utils import make_alembic_config, tmp_database
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

=======
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from core.settings import config
from tests.utils import make_alembic_config, tmp_database

>>>>>>> a0a9e11 (Fix folders)

@pytest.fixture(scope="package", name="pg_url")
def pg_url_fixture() -> str:
    """
<<<<<<< HEAD
    Create URL for test database with localhost.
    
    :return: URL with database.
=======
    Формирование URL для тестовой БД с localhost
>>>>>>> a0a9e11 (Fix folders)
    """
    config.DB_HOST = "localhost"
    return config.dsn


@pytest.fixture(name="postgres")
def postgres_fixture(pg_url: str) -> Iterator[str]:
    """
<<<<<<< HEAD
    Create main URL for test database.

    :param pg_url: URL with localhost on previous fixture.
    :return: main URL for test database.
=======
    На вход принимается pg_url из предыдущей фикстуры с localhost.
    Эти параметры передаем в контекстный менеджер tmp_database,
    возвращаем - новый URL с новым именем для тестовой БД
>>>>>>> a0a9e11 (Fix folders)
    """
    with tmp_database(pg_url, db_name="test_db") as tmp_url:
        yield tmp_url


@pytest.fixture(name="postgres_engine")
def postgres_engine_fixture(
    postgres: str,
) -> Iterator[Engine]:
    """
<<<<<<< HEAD
    Create engine for test database.

    :param postgres: main URL for test database on previous fixture.
    :return: engine for connect with test database.
=======
    На вход принимается полностью сформированный тестовый URL
    из предыдущей фикстуры и создается engine
>>>>>>> a0a9e11 (Fix folders)
    """
    engine = create_engine(postgres, echo=False)
    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture(name="alembic_config")
def alembic_config_fixture(postgres: str) -> Config:
    """
<<<<<<< HEAD
    Update alembic config for test database.

    :param postgres: main URL for test database on postgres_fixture.
    :return: alembic config for test database.
    """
    return make_alembic_config(postgres, "database")
=======
    На вход принимаем полностью сформированный тестовый URL
    и передается в функцию, которая преобразовывает alembic 
    как тестовый для тестов с миграциями
    """
    return make_alembic_config(postgres)
>>>>>>> a0a9e11 (Fix folders)
