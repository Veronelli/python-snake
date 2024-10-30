from enum import StrEnum
from src.common import Singleton
import time
from typing import TYPE_CHECKING


from src.game.player import Snake
from src.settings import Settings

if TYPE_CHECKING:
    from typing import Any

__all__ = ('Game',)


class Game(metaclass=Singleton):
    '''
    Snake game, this is the main class of the game, it is a singleton class
    '''

    class StatusGame(StrEnum):
        '''
        Enum to represent reproducing game status

        '''

        PLAYING = 'playing'
        PAUSED = 'paused'

    def __init__(
        self,
        game_settings: Settings,
    ) -> None:
        self._max_score = 100
        self._speed = 1
        self._state = Game.StatusGame.PAUSED

        player_settings = (
            self.game_settings.PLAYER
        )
        self.player = Snake(
            position=player_settings.POSITION,
            direction=player_settings.DIRECTION,
            direction_text=player_settings.DIRECTION_TEXT,
        )
        self.game_settings = game_settings

    def start(self) -> None:
        '''
        Start the game
        '''
        self._state = Game.StatusGame.PLAYING
        while (
            self._state == Game.StatusGame.PLAYING
        ):
            time.sleep(
                self.game_settings.GAME_SPEED
            )
