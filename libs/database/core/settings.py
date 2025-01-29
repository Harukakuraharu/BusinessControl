from pathlib import Path

<<<<<<< HEAD
from pydantic import Field, computed_field
=======
from pydantic import computed_field
>>>>>>> a0a9e11 (Fix folders)
from pydantic_settings import BaseSettings


class Config(BaseSettings):
<<<<<<< HEAD
    """Pull env config"""
=======
>>>>>>> a0a9e11 (Fix folders)

    ROOT_DIR: Path = Path(__file__).parent.parent.resolve()

    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "user"
    POSTGRES_DB: str = "db"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    REDIS_HOST: str = "localhost"

<<<<<<< HEAD
    REDIS_HOST: str = "localhost"

    SECRET_KEY: str = Field(default="")
    ALGORITHM: str = Field(default="")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 100

=======
>>>>>>> a0a9e11 (Fix folders)
    @computed_field
    def async_dsn(self) -> str:
        """URL for async commection"""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.POSTGRES_DB}"
        )

    @computed_field
    def dsn(self) -> str:
        """URL for connections"""
        return (
            f"postgresql://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.POSTGRES_DB}"
        )

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3f2822f (Complete servis with admin and company)
    @computed_field
    def redis_url(self) -> str:
        """URL for redis"""
        return f"redis://{self.REDIS_HOST}:6379/1"

<<<<<<< HEAD
=======
>>>>>>> a0a9e11 (Fix folders)
=======
>>>>>>> 3f2822f (Complete servis with admin and company)

config = Config()
