from enum import StrEnum
from src.common import Singleton

from typing import TYPE_CHECKING

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

    def __init__(self, *args: 'Any') -> None:
        self._max_score = 100
        self._speed = 1
        self._paused = Game.StatusGame.PAUSED
        self.other_settings = args

    def start(self) -> None:
        '''
        Start the game
        '''
        self._paused = Game.StatusGame.PLAYING
