__all__ = ('Table',)

from src.game.elements.wall import Wall


class Table:
    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows

        self.walls = [Wall(x=column, y=0) for column in range(0, columns + 1)]
        self.walls += [Wall(x=0, y=row) for row in range(0, rows)]
        self.walls += [Wall(x=columns - 1, y=row) for row in range(0, rows)]
        self.walls += [
            Wall(x=column, y=rows) for column in range(0, columns + 1)
        ]


if __name__ == "__main__":
    table = Table(columns=10, rows=10)
    print(
        [f'(format={wall.character} {wall.x} {wall.y})' for wall in table.walls]
    )
