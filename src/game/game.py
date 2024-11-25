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
        self.snake = Snake(
            position=player_settings.POSITION,
            direction=player_settings.DIRECTION,
            direction_text=player_settings.DIRECTION_TEXT,
            speed=player_settings.SPEED,
        )

        self.game_settings = game_settings
        self.table = Table(
            columns=game_settings.WIDTH,
            rows=game_settings.HEIGHT,
            player_settings=player_settings,
        )

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
            position_x = int(element["x"])
            position_y = int(element["y"])
            character = element["character"]
            name = element['name']
            self._screen.addstr(position_x, position_y, character)
            if name is 'Snake':
                if not self.table.snake.direction == [0, 0]:
                    self._screen.addstr(
                        int(position_x) - self.table.snake.direction[0],
                        int(position_y) - self.table.snake.direction[1],' ')
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


        game_state = PlayingState()
        height, width = self._screen.getmaxyx()
        self.__update()
        # return None
        # while isinstance(self._state, PlayingState):
        #     game_state.update(game=self)
        #     key = self._screen.getch()
        #
        #     self._screen.addstr(
        #         0,
        #         0,
        #         "Press 'q' to exit, and 'p' to pause",
        #     )
        #     self._screen.addstr(
        #         0,
        #         width - 5,
        #         f"{self.snake.direction_text}",
        #     )
        #
        #     self.snake.expect_inputs(key=key)
        #
        #     self._screen.refresh()
        #     self._screen.clrtobot()
        #     bottom_menu = "=" * width
        #     self._screen.addstr(height - 2, 0, bottom_menu)
        #     self._screen.addstr(
        #         int(self.snake.x),
        #         int(self.snake.y),
        #         self.snake.snake[0]["character"],
        #     )
        #     self._screen.addstr(
        #         5,
        #         0,
        #         "#" * (self.game_settings.WIDTH + 4),
        #     )
        #
        #     for i in range(1, self.game_settings.HEIGHT + 1):
        #         draw_index = i + 5
        #         self._screen.addstr(draw_index, 0, "||")
        #         if i == self.snake.snake[0]["position"][1]:
        #             self._screen.addstr(
        #                 self.snake.snake[0]["position"][0],
        #                 self.snake.snake[0]["position"][1],
        #                 self.snake.snake[0]["character"],
        #             )
        #
        #         self._screen.addstr(
        #             draw_index,
        #             self.game_settings.WIDTH + 2,
        #             "||",
        #         )
        #     position_x = int(f"{(self.snake.x - 6):.0f}")
        #     position_y = int(f"{(self.snake.y - 2):.0f}")
        #     self._screen.addstr(
        #         5,
        #         self.game_settings.WIDTH + 2,
        #         "||",
        #     )
        #     self._screen.addstr(
        #         self.game_settings.HEIGHT + 6,
        #         0,
        #         "#" * (self.game_settings.WIDTH + 4),
        #     )
        #     if (
        #         position_x > self.game_settings.WIDTH
        #         or position_y > self.game_settings.HEIGHT
        #         or position_x < 0
        #         or position_y < 0
        #     ):
        #         self.snake.collided = True
        #
        #     self._screen.addstr(
        #         height - 2,
        #         int(width / 2) - 5,
        #         f"[x: {position_x},y: {position_y}]",
        #     )
