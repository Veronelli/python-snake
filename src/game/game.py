import curses
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

    'Register all events that will be listening'

    class StatusGame(StrEnum):
        '''
        Enum to represent reproducing game status

        '''

        PLAYING = 'playing'
        PAUSED = 'paused'

    def __init__(
        self,
        screen: curses.window,
        game_settings: Settings,
    ) -> None:
        self._max_score = 100
        self._speed = 1
        self._screen = screen
        self._state = Game.StatusGame.PAUSED

        player_settings = game_settings.PLAYER
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
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(True)
        self._screen.nodelay(True)
        height, width = self._screen.getmaxyx()
        while (
            self._state == Game.StatusGame.PLAYING
        ):
            self._screen.clrtobot()
            key = self._screen.getch()

            self._screen.addstr(
                0,
                0,
                "Press 'q' to exit, and 'p' to pause",
            )
            self._screen.addstr(
                0,
                width - 5,
                f"{self.player.direction_text}",
            )
            self.player.expect_inputs(key=key)
            curses.napms(
                self.game_settings.GAME_SPEED
            )
            self._screen.refresh()
