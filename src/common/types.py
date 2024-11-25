from typing import TypedDict


class ElementType(TypedDict, total=False):
    name: str
    character: str
    x: float
    y: float