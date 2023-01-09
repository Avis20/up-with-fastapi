

from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    BACKEND_PORT: int


@lru_cache
def get_settings():
    return Settings()
