from __future__ import annotations
import numpy as np
from enum import Enum
from aoc_lib.basic.types import *
from aoc_lib.data_structs.coord import *


X = 0
Y = 1
Z = 2

ROW = 0
COL = 1


N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
NE = cross_sum(N, E)
NW = cross_sum(N, W)
SE = cross_sum(S, E)
SW = cross_sum(S, W)

CARDINAL = N, S, E, W
ORDINAL = NW, NE, SE, SW


def pretty_print_grid(grid: list[list[T]], spacer: str = ""):
    for line in grid:
        print(spacer.join(line))
    print()


def print_path(grid: Grid | list[list[T]], start: Coord2D, goal: Coord2D, path: list[Coord2D]):
    for location in path:
        grid[location.row][location.col] = "•"
    grid[start.row][start.col] = "S"
    grid[goal.row][goal.col] = "G"
    pretty_print_grid(grid)


def string_to_grid(string: str, dtype=str, split_func=lambda row: list(row)):
    '''Returns a numpy matrix from a single plain string.
    String's rows must be separated by '\n'. Callback defines row elements splitting.'''
    return np.asarray([split_func(row) for row in string.split("\n")], dtype=dtype)


def generate_grid(shape: tuple[int, int], fill_value: str | int | bool):
    '''Returns a matrix of given shape filled with given fill value.
    Example: create_filled_with((10, 10), 0)'''
    if fill_value == True:
        return np.ones(shape, dtype=bool)
    elif fill_value == False:
        return np.zeros(shape, dtype=bool)
    elif is_int(fill_value) or fill_value.isdigit():
        return np.full(shape, fill_value, dtype=int)
    else:
        return np.full(shape, fill_value)


def grid_has_location(location: tuple[int, int], shape: tuple[int, int]):
    return 0 <= location[X] < shape[X] and 0 <= location[Y] < shape[Y]


def list_neighbours(
    location: tuple[int, int],
    shape: tuple[int, int],
    include_diagonals=False,
    include_outside=False
):
    relative_neighbours = CARDINAL + (ORDINAL if include_diagonals else [])
    neighbours = [cross_sum(location, neighbour) for neighbour in relative_neighbours]
    if include_outside:
        return neighbours
    return [neighbour for neighbour in neighbours if grid_has_location(neighbour, shape)]


def list_orthogonal_neighbours(location: tuple[int, int], shape: tuple[int, int]):
    left   = list(reversed([(i, location[Y]) for i in range(location[X])]))
    top    = list(reversed([(location[X], i) for i in range(location[Y])]))
    right  = [(i, location[Y]) for i in range(*sorted([location[X] + 1, shape[X]]))]
    bottom = [(location[X], i) for i in range(*sorted([location[Y] + 1, shape[Y]]))]
    return [left, right, top, bottom]


class Grid():
    '''Returns a numpy grid wrapper with many useful methods and syntax sugars.
    Grid can be generated from a single plain string or with given shape and fill_value.
    Usage examples:
        Grid(string=raw_input, dtype=int)
        Grid(shape=(6, 6), fill_value=False)

    Examples of useful numpy methods:
        np.where(condition) -> returns indexes where condition is met.
        np.where(np_matrix == number) -> [[i1_row, i2_row], [i1_col, i2_col]]

        np.any(condition) -> returns boolean if any element meets condition.
        np.all(condition) -> returns boolean if all elements meet condition.
        np.all(np_matrix > number) -> False
        np.all(np_matrix > number, axis=Grid.row_axis) -> [True False False False False]
    '''
    def __init__(self, **kwargs) -> None:
        self.grid = self._generate_grid(**kwargs)
        self.dtype = kwargs["dtype"] if "dtype" in kwargs else type(kwargs["fill_value"])
        self.shape = self.grid.shape
        self.rows_len = self.shape[ROW]
        self.cols_len = self.shape[COL]
        self.locations = list(np.ndindex(self.grid.shape))
        self.len = len(self.locations)

    def __repr__(self) -> str:
        pretty_print_grid(self.grid.tolist(), " ")
        return ""

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __getitem__(self, key):
        return self.grid[key]

    @property
    def value_by_location(self):
        return {location: self.grid[location] for location in self.locations}

    def tolist(self):
        return self.grid.tolist()

    def invert(self):
        self.grid = ~self.grid

    def sum(self):
        '''Returns the sum of all matrix elements.'''
        return np.sum(self.grid)

    def has_location(self, location: tuple[int, int]):
        return grid_has_location(location, self.shape)

    def is_in_grid(self, location: tuple[int, int]):
        return self.has_location(location)

    def list_indexes_where(result):
        '''Returns a list of index tuples for given results of numpy's where method.
        Example: list_indexes_where(np.where(matrix > 0))'''
        indexes = []
        for i in range(len(result[0])):
            row = result[ROW][i]
            col = result[COL][i]
            indexes.append((row, col))
        return indexes

    @property
    def neighbours_by_location(self):
        return {location: self.list_neighbours(location) for location in self.locations}

    @property
    def orthogonal_neighbours_by_location(self):
        return {location: self.list_orthogonal_neighbours(location) for location in self.locations}

    def list_neighbours(
        self, location: tuple[int, int], include_diagonals=False, include_outside=False
    ):
        return list_neighbours(location, self.shape, include_diagonals, include_outside)

    def list_orthogonal_neighbours(self, location: tuple[int, int]):
        return list_orthogonal_neighbours(location, self.shape)

    def _generate_grid(self, **kwargs):
        if "string" in kwargs.keys():
            return string_to_grid(**kwargs)
        return generate_grid(**kwargs)


HashmapGridMapType = dict[tuple[int, int], str | int | bool]


def pretty_print_hashmap_grid(hashmap_grid: HashmapGrid | HashmapGridMapType, shape=None):
    if shape:
        pretty_print_grid(hashmap_to_grid(hashmap_grid, shape))
    else:
        pretty_print_grid(hashmap_to_grid(hashmap_grid.map, hashmap_grid.shape))


def hashmap_to_grid(hashmap: HashmapGridMapType, shape: tuple[int, int], dtype=str):
    fill_value = " "
    if dtype == int:
        fill_value = 1
    if dtype == bool:
        fill_value = True

    grid = Grid(shape=shape, fill_value=fill_value)
    for location, value in hashmap.items():
        grid[location] = value
    return grid


class HashmapGrid():
    def __init__(self, string: str, dtype=str, split_func=lambda row: list(row)) -> None:
        '''Returns a hashmap wrapper generated from a single plain string.
        String's rows must be delimited by '\n'. split_func defines how row elements are split.'''
        self.map, self.shape = self._string_to_map(string=string, dtype=dtype, split_func=split_func)
        self.dtype = dtype
        self.rows_len = self.shape[ROW]
        self.cols_len = self.shape[COL]
        self.locations = list(self.map.keys())
        self.len = len(self.locations)

    def __repr__(self) -> str:
        pretty_print_grid(self.hashmap_to_grid(), " ")
        return ""

    def __setitem__(self, key, value):
        self.map[key] = value

    def __getitem__(self, key):
        return self.map[key]

    def keys(self):
        return self.map.keys()

    def values(self):
        return self.map.values()

    def items(self):
        return self.map.items()

    def hashmap_to_grid(self):
        return hashmap_to_grid(self.map, self.shape, self.dtype)

    def has_location(self, location: tuple[int, int]):
        return location in self.map

    def is_in_map(self, location: tuple[int, int]):
        return self.has_location(location)

    @property
    def neighbours_by_location(self):
        return {location: self.list_neighbours(location) for location in self.map}

    @property
    def orthogonal_neighbours_by_location(self):
        return {location: self.list_orthogonal_neighbours(location) for location in self.map}

    def list_neighbours(
        self, location: tuple[int, int], include_diagonals=False, include_outside=False
    ):
        return list_neighbours(location, self.shape, include_diagonals, include_outside)

    def list_orthogonal_neighbours(self, location: tuple[int, int]):
        return list_orthogonal_neighbours(location, self.shape)

    def _string_to_map(self, **kwargs):
        grid = Grid(**kwargs)
        hashmap = {}
        for coord in grid.locations:
            hashmap[coord] = grid[coord]
        return hashmap, grid.shape


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "•"


class Maze:
    def __init__(self, grid: list[list[str]], start: Coord2D, goal: Coord2D) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.shape = (self.rows, self.cols)
        self.locations = list(np.ndindex(self.shape))
        self.start = start
        self.goal = goal

    def __repr__(self):
        output = ""
        for line in self.grid:
            output += "".join(line) + "\n"
        return output

    def has_location(self, location: tuple[int, int]):
        return location in self.locations

    def test_goal(self, location: Coord2D) -> bool:
        return (location.row, location.col) == (self.goal.row, self.goal.col)

    def _successor_is_viable(self, current: Coord2D, successor: Coord2D):
        row, col = successor
        return self.grid[row][col] != Cell.BLOCKED

    def list_successors(self, loc: Coord2D) -> list[Coord2D]:
        locations: list[Coord2D] = []
        condition_by_potential_location = {
            Coord2D(loc.row + 1, loc.col): loc.row + 1 < self.rows,
            Coord2D(loc.row - 1, loc.col): loc.row - 1 >= 0,
            Coord2D(loc.row, loc.col + 1): loc.col + 1 < self.cols,
            Coord2D(loc.row, loc.col - 1): loc.col - 1 >= 0,
        }
        for potential_location, condition in condition_by_potential_location.items():
            if condition and self._successor_is_viable(loc, potential_location):
                locations.append(potential_location)

        return locations

    def mark(self, path: list[Coord2D]):
        for location in path:
            self.grid[location.row][location.col] = Cell.PATH
        self.grid[self.start.row][self.start.col] = Cell.START
        self.grid[self.goal.row][self.goal.col] = Cell.GOAL

    def clear(self, path: list[Coord2D]):
        for location in path:
            self.grid[location.row][location.col] = Cell.EMPTY
        self.grid[self.start.row][self.start.col] = Cell.START
        self.grid[self.goal.row][self.goal.col] = Cell.GOAL
