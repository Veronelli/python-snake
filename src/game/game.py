import curses
from enum import StrEnum
from src.common import Singleton
from typing import TYPE_CHECKING
from math import floor, ceil


from src.game.elements import Snake, Element
from src.game.state import GameState, PlayingState
from src.game.table import Table
from src.settings import Settings, settings

if TYPE_CHECKING:
    from typing import Any

__all__ = ("Game",)


class Game(metaclass=Singleton):
    """
    Snake game, this is the main class of the game, it is a singleton class
    """

    "Register all events that will be listening"
    class StatusGame(StrEnum):
        """
        Enum to represent reproducing game status

        """

        PLAYING = "playing"
        PAUSED = "paused"

    def __init__(
        self,
        screen: curses.window,
        game_settings: Settings,
    ) -> None:
        self._max_score = 100
        self._speed = 1
        self._screen = screen
        self._state: GameState = PlayingState()
        player_settings = game_settings.PLAYER
        self.game_settings = game_settings
        self.table = Table(
            columns=game_settings.WIDTH,
            rows=game_settings.HEIGHT,
            player_settings=player_settings,
        )
        self.win1 = self._screen.subwin(self.game_settings.HEIGHT, self.game_settings.WIDTH, 0, 0)

    def change_state(self, state: GameState) -> None:
        """
        Change the state of the game
        """
        self._state = state

    def __draw(self) -> None:
        """
        Draw the game
        """
        self._screen.clrtobot()
        for element in self.table.items:
            position_x = int(element.x)
            position_y = int(element.y)
            character = element.character
            name = element.name
            self._screen.addstr(position_x, position_y, character)
            if name is 'Snake':
                if not self.table.snake.direction == [0, 0]:
                    self._screen.addstr(
                        int(position_x) - self.table.snake.direction[0],
                        int(position_y) - self.table.snake.direction[1],' ')
        self.table.handle_event()
        self._screen.refresh()



    def __update(self) -> None:
        while(True):
            key = self._screen.getch()
            self.table.capture_keys(key=key)
            self.table.make_move()
            self.__draw()
            curses.napms(self.game_settings.GAME_SPEED)


    def start(self) -> None:
        """
        Start the game
        """
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(True)
        self._screen.nodelay(True)
        self.__update()
