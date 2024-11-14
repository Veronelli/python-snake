__all__ = ('Table',)

from src.game.elements import Snake, Wall
from src.settings import Player


class Table:
    def __init__(self, columns: int, rows: int, player_settings: Player):
        self.columns = columns
        self.rows = rows

        self.walls = [Wall(x=column, y=0) for column in range(0, columns + 1)]
        self.walls += [Wall(x=0, y=row) for row in range(0, rows)]
        self.walls += [Wall(x=columns - 1, y=row) for row in range(0, rows)]
        self.walls += [
            Wall(x=column, y=rows) for column in range(0, columns + 1)
        ]

        self.player = Snake(
            postion=player_settings.POSITION,
            direction=player_settings.DIRECTION,
            direction_text=player_settings.DIRECTION_TEXT,
            speed=player_settings.SPEED,
        )
