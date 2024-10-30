from pydantic_settings import (
    BaseSettings,
)


class Settings(BaseSettings):
    REFRESH_LOOP: int = 15
    TIMEOUT: int = 60000
