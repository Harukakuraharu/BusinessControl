from pydantic import Field, computed_field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """Pull env config"""

    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "user"
    POSTGRES_DB: str = "db"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    SECRET_KEY: str = Field(default="")
    ALGORITHM: str = Field(default="")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 100
    ADMIN_PANEL: str = "admin_panel"

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


config = Config()
