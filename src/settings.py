from pydantic_settings import (
    BaseSettings,
)

from src.common import DirectionPlayer

__all__ = (
    'Settings',
    'settings',
)


class Player(BaseException):
    POSITION: list[int, int] = [50, 50]
    DIRECTION: list[int, int] = [0, 0]
    DIRECTION_TEXT: DirectionPlayer = (
        DirectionPlayer.RIGHT
    )


class Settings(BaseSettings):
    GAME_SPEED: int = 1
    TIMEOUT: int = 60000
    PLAYER: Player = Player()
    DIMENCION: str = '16x16'


settings = Settings()
