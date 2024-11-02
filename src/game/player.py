from src.common import DirectionPlayer
from src.game.type import SnakeType

__all__ = ("Snake",)


class Snake:

    snake: list[SnakeType] = []

    def __init__(
        self,
        position: list[float],
        direction: list[int],
        direction_text: str,
        speed: float,
    ) -> None:
        self.position = position
        self.direction: list[int] = direction
        self.direction_text: str = direction_text
        self.speed: float = speed
        self.snake.append(
            {
                "character": "O",
                "part": 0,
                "position": self.position,
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
        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed
        self.snake[0]["position"] = [
            int(self.position[0]),
            int(self.position[1]),
        ]

    def get_position(self) -> None:
        return self.position

    def expect_inputs(self, key: int) -> None:
        """
        Listen to any inputs and change direction of the snake
        """

        if key == ord("w"):
            self.change_direction(-1, 0)
            self.direction_text = DirectionPlayer.RIGHT
        elif key == ord("s"):
            self.change_direction(1, 0)
            self.direction_text = DirectionPlayer.LEFT
        elif key == ord("d"):
            self.change_direction(0, 1)
            self.direction_text = DirectionPlayer.UP
        elif key == ord("a"):
            self.change_direction(0, -1)
            self.direction_text = DirectionPlayer.DOWN
