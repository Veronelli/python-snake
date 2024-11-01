from logging import getLogger
from typing import Any
from src.game.game import Game
import curses

logger = getLogger(__name__)


class GameState:
    """Abstract class of game states"""

    def handle_input(self, game, input):
        raise NotImplementedError

    def update(self, game):
        raise NotImplementedError

    def enter(self, game):
        raise NotImplementedError


class PausedState(GameState):
    """Status to handle in pause status"""

    def handle_input(
        self, game: Game, input: Any
    ):
        if input == 'p':
            logger.warning('Resuming game...')
            game.change_state(PlayingState())

    def update(self, game: Game):
        pass

    def enter(self, game: Game):
        logger.warning("Paused state")


class GameOverState(GameState):
    """Status to handle in game over status"""

    def handle_input(
        self, game: Game, input: Any
    ):
        if input == 'q':
            logger.warning('Quitting game...')
            game.quit()

    def update(self, game: Game):
        pass

    def enter(self, game: Game):
        logger.warning("Game over state")


class PlayingState(GameState):
    """Status to handle in playing status"""

    def handle_input(
        self, game: Game, input: Any
    ):
        if input == 'p':
            logger.warning('Pausing game...')
            game.change_state(PausedState())
        elif input == 'q':
            logger.warning('Quitting game...')
            game.change_state(GameOverState())

    def update(self, game: Game):
        game.snake.move()
        if game.snake.collided():
            game.change_state(GameOverState())

    def enter(self, game: Game):
        logger.warning("Playing state")
