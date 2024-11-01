import curses
from typing import Any
from src.game.game import Game

__all__ = ("Application",)


class Application:
    def __init__(
        self,
        *args: Any,
    ) -> None:
        """
        Aplication initializer that allow to set all main settings on run time process
        """
        from src.settings import settings

        self.game_settings = settings

    def run(self) -> None:
        game = curses.wrapper(
            Game,
            game_settings=self.game_settings)
        game.start()
