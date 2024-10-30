from pydantic_settings import (
    BaseSettings,
)

__all__ = (
    'Settings',
    'settings',
)


class Player(BaseException):
    POSITION: list[int, int] = [50, 50]
    DIRECTION: list[int, int] = [0, 0]
    DIRECTION_TEXT: str = 'right'


class Settings(BaseSettings):
    GAME_SPEED: float = 0.2
    TIMEOUT: int = 60000
    PLAYER: Player = Player()


settings = Settings()
