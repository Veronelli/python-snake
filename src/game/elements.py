from dataclasses import asdict
from typing import Any, TYPE_CHECKING
from src.common import DirectionPlayer
from src.game.type import SnakeType
from src.settings import settings
import random

__all__ = ('Snake', 'Wall')

if TYPE_CHECKING:
    from src.game.table import Table


class Element:
    name: str


    def collision(self, table: 'Table', element: 'Element') -> None:
        '''
        Detect collision between two elements
        '''
        return

    def on_collision(self, element: 'Element') ->None:
        return

    def get_position(self) -> Any:
        '''
        Get the position of the element
        '''
        raise NotImplementedError('get_position method must be implemented')

    def to_dict(self) -> dict[str, Any]:
        return asdict(self) if hasattr(self, '__dataclass_fields__') else self.__dict__


class Snake(Element):

    snake: list[SnakeType] = []
    def __init__(
        self,
        position: list[float],
        direction: list[int],
        direction_text: str,
        speed: float
    ) -> None:
        self.x = position[0]
        self.y = position[1]
        self.character = "O"
        self.direction: list[int] = direction
        self.direction_text: str = direction_text
        self.speed: float = speed
        self.name = 'Snake'

        self.snake.append(
            {
                "character": "O",
                "part": 0,
                "position": [self.x, self.y],
            }
        )
        self._collided: bool = False

    list_collision = [
        "Wall",
        "Food"
    ]

    @property
    def collided(self) -> bool:
        return self._collided

    @collided.setter
    def collided(self, collided: bool) -> None:
        self._collided = collided

    def change_direction(self, dx: int, dy: int) -> None:
        self.direction = (dx, dy)

    def move(self) -> None:
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        self.snake[0]["position"] = [
            int(self.x),
            int(self.y),
        ]

    def collision(self, table: 'Table', element: Element) -> None:
        """
        Handles the collision logic between the current object and another element.

        This method checks if the current object (`self`) collides with another
        specified `element`. If the `element` is of a type listed in the
        `list_collision` attribute of the current object, the `on_collision`
        method of the `element` is triggered. The `table` is passed as a
        parameter to provide context for the collision.

        Args:
            table (Table): The table or environment in which the collision occurs.
            element (Element): The other element involved in the potential collision.

        Returns:
            None: This method does not return a value. It only executes the
                  collision logic.

        Notes:
            - The method skips collision processing if `self` and `element` are
              the same object.
            - The `list_collision` attribute is expected to be a list of type names
              (as strings) that the current object can collide with.

        Example:
            If `self.list_collision` is `["Player", "Enemy"]`, and `element` is
            an instance of a class with the name "Player", the `on_collision`
            method of `element` will be called.
        """
        if self == element:
            return
        if (
                self.get_position() == element.get_position()
        ):
            element.on_collision(table=table, element=self)

    def get_position(self) -> list[float]:
        return [int(self.x), int(self.y)]

    def expect_inputs(self, key: int) -> None:
        """
        Listen to any inputs and change direction of the snake
        """
        if key == ord("w"):
            self.change_direction(dx=-1, dy=0)
            self.direction_text = DirectionPlayer.RIGHT
        elif key == ord("s"):
            self.change_direction(dx=1, dy=0)
            self.direction_text = DirectionPlayer.LEFT
        elif key == ord("d"):
            self.change_direction(dx=0, dy=1)
            self.direction_text = DirectionPlayer.UP
        elif key == ord("a"):
            self.change_direction(dx=0, dy=-1)
            self.direction_text = DirectionPlayer.DOWN


class Wall(Element):

    def __init__(self, x, y):
        self.name = 'Wall'
        self.x = x
        self.character = '#'
        self.y = y

    def __str__(self):
        return self.character

    def get_position(self) -> list[str, Any]:
        return [self.x, self.y]

    def on_collision(self, table: 'Table', element: 'Element') ->None:
        if type(element).__name__ == 'Snake':
            table.stop = True

class Food(Element):
    def __init__(self):
        self.name = 'Food'
        x = random.randint(1, settings.WIDTH - 2)
        y = random.randint(1, settings.HEIGHT - 2)
        self.character = 'X'
        self.x = x
        self.y = y

    def get_position(self) -> list[str, Any]:
        return [self.x, self.y]

    def respawn(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return self.character

    def on_collision(self, table: 'Table', element: 'Element') ->None:
        if type(element).__name__ == 'Snake':
            table.verify_respawn_food()
            element.speed += 0.002
