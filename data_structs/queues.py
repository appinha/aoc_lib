from aoc_lib.basic.types import *
from typing import Deque
from heapq import heappush, heappop


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        return not self.items

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.popleft()

    def __repr__(self) -> str:
        return repr(self.items)


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    @property
    def empty(self) -> bool:
        return not self.items

    def push(self, item: T) -> None:
        heappush(self.items, item)  # in by priority

    def pop(self) -> T:
        return heappop(self.items)  # out by priority

    def __repr__(self) -> str:
        return repr(self.items)
