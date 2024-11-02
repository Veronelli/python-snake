from typing import TypedDict


class SnakeType(TypedDict, total=False):
    character: str
    part: int
    position: list[int, int]
