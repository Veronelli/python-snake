__all__ = 'Wall'


class Wall:
    character = '#'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.character
