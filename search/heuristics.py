from math import sqrt
from typing import Callable
from aoc_lib.data_structs.coord import Coord2D


def euclidean_distance(goal: Coord2D) -> Callable[[Coord2D], float]:
    def distance(location: Coord2D) -> float:
        x_dist: int = location.col - goal.col
        y_dist: int = location.row - goal.row
        return sqrt((x_dist**2) + (y_dist**2))

    return distance


def calc_euclidean_distance(origin: tuple[int, int], destination: tuple[int, int]) -> float:
    return euclidean_distance(Coord2D(*destination))(Coord2D(*origin))


def manhattan_distance(goal: Coord2D) -> Callable[[Coord2D], float]:
    def distance(location: Coord2D) -> float:
        x_dist: int = abs(location.col - goal.col)
        y_dist: int = abs(location.row - goal.row)
        return x_dist + y_dist

    return distance


def calc_manhattan_distance(origin: tuple[int, int], destination: tuple[int, int]) -> float:
    return manhattan_distance(Coord2D(*destination))(Coord2D(*origin))
