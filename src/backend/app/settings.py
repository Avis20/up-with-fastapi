from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "phresh"

    BACKEND_PORT: int = 5000

    PG_MASTER_USER: str = "fa_ddd_user"
    PG_MASTER_PASSWORD: str = "fa_ddd_pass"

    @property
    def db_master_uri(self) -> str:
        return (
            f"postgresql+psycopg2://{self.PG_MASTER_USER}:"
            f"{self.PG_MASTER_PASSWORD}@{self.PG_MASTER_HOST}:{self.PG_MASTER_PORT}/"
            f"{self.PG_MASTER_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
