from __future__ import annotations
from aoc_lib.basic.types import *
from typing import Deque


class GraphNode(Generic[T]):
    def __init__(
        self, state: T, parent: Optional[GraphNode], cost: float = 0.0, heuristic: float = 0.0,
    ) -> None:
        self.state: T = state
        self.parent: Optional[GraphNode] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __repr__(self) -> str:
        return f"GraphNode(state: {self.state}, cost: {self.cost}, heuristic: {self.heuristic})"

    def __lt__(self, other: GraphNode) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node: GraphNode[T]) -> list[T]:
    path = Deque([node.state])
    while node.parent is not None:  # work backwards from end to front
        node = node.parent
        path.appendleft(node.state)
    return path
