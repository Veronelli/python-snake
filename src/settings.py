from pydantic_settings import (
    BaseSettings,
)

from src.common import DirectionPlayer

__all__ = (
    "Settings",
    "settings",
)


class Player(BaseException):
    POSITION: list[int, int] = [6, 2]
    DIRECTION: list[int, int] = [0, 0]
    DIRECTION_TEXT: DirectionPlayer = DirectionPlayer.RIGHT
    SPEED: float = 0.005


class Settings(BaseSettings):
    GAME_SPEED: int = 1
    TIMEOUT: int = 60000
    PLAYER: Player = Player()
    WIDTH: int = 20
    HEIGHT: int = 20


settings = Settings()
