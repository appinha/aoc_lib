from typing import TypeVar, Generic, List


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def __repr__(self) -> str:
        return repr(self.items)
