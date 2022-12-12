from aoc_lib.basic.types import *


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def __repr__(self) -> str:
        return repr(self.items)

    @property
    def empty(self) -> bool:
        return not self.items

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
