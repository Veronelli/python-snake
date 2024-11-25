from dataclasses import asdict
from typing import Any
from src.common import DirectionPlayer
from src.game.type import SnakeType
from src.settings import settings
import random

__all__ = ('Snake', 'Wall')


class Element:
    name: str


    def collition(self, element: object) -> None:
        '''
        Detect collition between two elements
        '''
        raise NotImplementedError('collition method must be implemented')

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

    def get_position(self) -> list[float]:
        return [self.x, self.y]

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

    def collition(self, object: Element) -> None:
        ...
        # if

    def get_position(self) -> list[str, Any]:
        return [self.x, self.y]


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

    def collition(self, object: Element) -> None: ...
