from src.common import DirectionPlayer

__all__ = ('Snake',)


class Snake:

    def __init__(
        self,
        position: list[int],
        direction: list[int],
        direction_text: str,
    ) -> None:
        self.position = position
        self.direction: list[int] = direction
        self.direction_text: str = direction_text

    def change_direction(
        self, dx: int, dy: int
    ) -> None:
        self.direction = (dx, dy)

    def move(self) -> None:
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

    def get_position(self) -> None:
        return self.position

    def expect_inputs(self, key: int) -> None:
        '''
        Listen to any inputs and change direction of the snake
        '''

        if key == ord('w'):
            self.change_direction(0, -1)
            self.direction_text = (
                DirectionPlayer.UP
            )
        elif key == ord('s'):
            self.change_direction(0, 1)
            self.direction_text = (
                DirectionPlayer.DOWN
            )
        elif key == ord('a'):
            self.change_direction(-1, 0)
            self.direction_text = (
                DirectionPlayer.LEFT
            )
        elif key == ord('d'):
            self.change_direction(1, 0)
            self.direction_text = (
                DirectionPlayer.RIGHT
            )
