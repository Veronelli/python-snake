__all__ = ('Table',)

from src.common.types import ElementType
from src.game.elements import Snake, Wall, Food
from src.settings import Player
import random
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from curses import window


class Table:
    same_position: Callable[[list[float], list[float]], bool] = staticmethod(
        lambda position_1, position_2: position_1 == position_2
    )

    def __init__(self, columns: int, rows: int, player_settings: Player):
        self.columns = columns
        self.rows = rows

        self.walls = [Wall(x=column, y=0) for column in range(0, columns + 1)]
        self.walls += [Wall(x=0, y=row) for row in range(0, rows)]
        self.walls += [Wall(x=columns - 1, y=row) for row in range(0, rows)]
        self.walls += [
            Wall(x=column, y=rows) for column in range(0, columns + 1)
        ]
        self.food = Food()

        self.snake = Snake(
            position=player_settings.POSITION,
            direction=player_settings.DIRECTION,
            direction_text=player_settings.DIRECTION_TEXT,
            speed=player_settings.SPEED,
        )

    @property
    def items(self)-> list[ElementType]:
        yield self.snake.to_dict()
        yield self.food.to_dict()
        yield from (wall.to_dict() for wall in self.walls)

    def capture_keys(self, key: int) -> None:
        self.snake.expect_inputs(key=key)

    def make_move(self) -> None:
        self.snake.move()

    def verify_respawn_food(self):
        x = random.randint(1, self.columns - 1)
        y = random.randint(1, self.rows - 1)
        for wall in self.walls:
            if [x, y] == wall.get_position() and [
                x,
                y,
            ] == self.snake.get_position():
                self.verify_respawn_food()
            else:
                self.food.respawn(x, y)
