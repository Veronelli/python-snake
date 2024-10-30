import curses

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

    def expect_inputs(self) -> None:
        '''
        Listen to any inputs and change direction of the snake
        '''
        key = self.screen.getch()
        if key == curses.KEY_UP:
            self.change_direction(0, -1)
        elif key == curses.KEY_DOWN:
            self.change_direction(0, 1)
        elif key == curses.KEY_LEFT:
            self.change_direction(-1, 0)
        elif key == curses.KEY_RIGHT:
            self.change_direction(1, 0)
