import numpy as np
from aoc_lib.basic.numbers import *
from aoc_lib.basic.types import *


X = 0
Y = 1
Z = 2

ROW = 0
COL = 1


class HashmapGrid():
    def __init__(self, string: str, dtype, split_func=lambda row: row) -> None:
        '''Returns a hashmap from a single plain string.
        String's rows must be delimited by '\n'. split_func defines how row elements are split.'''
        self.grid = Grid(string, dtype, split_func)
        self.shape = self.grid.shape
        self.map = self._grid_to_map()
        self.locations = self.map.keys()
        self.len = len(self.locations)

    def __repr__(self) -> str:
        return repr(self.grid)

    def __getitem__(self, key):
        return self.map[key]

    def _grid_to_map(self):
        hashmap = {}
        for coord in self.grid.locations:
            hashmap[coord] = self.grid[coord]
        return hashmap

    def keys(self):
        return self.map.keys()

    def values(self):
        return self.map.values()

    def has_location(self, location: tuple[int, int]):
        return location in self.locations

    def is_in_map(self, location: tuple[int, int]):
        return self.has_location(location)

    @property
    def neighbours_by_location(self):
        return {location: self.get_neighbours(location) for location in self.map}

    @property
    def orthogonal_neighbours_by_location(self):
        return {location: self.get_orthogonal_neighbours(location) for location in self.map}

    def get_neighbours(self, location: tuple[int, int]):
        relative_neighbours = [
            (x, y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0) and abs(x) != abs(y)
        ]
        neighbours = [(neighbour[X] + location[X], neighbour[Y] + location[Y])
            for neighbour in relative_neighbours]
        return [neighbour for neighbour in neighbours if self.is_in_map(neighbour)]

    def get_orthogonal_neighbours(self, location: tuple[int, int]):
        left   = list(reversed([(i, location[Y]) for i in range(location[X])]))
        top    = list(reversed([(location[X], i) for i in range(location[Y])]))
        right  = [(i, location[Y]) for i in range(*sorted([location[X] + 1, self.shape[X]]))]
        bottom = [(location[X], i) for i in range(*sorted([location[Y] + 1, self.shape[Y]]))]
        return [left, right, top, bottom]


class Grid():
    '''Examples of useful numpy methods:
        np.where(condition) -> returns indexes where condition is met.
        np.where(np_matrix == number) -> [[i1_row, i2_row], [i1_col, i2_col]]

        np.any(condition) -> returns boolean if any element meets condition.
        np.all(condition) -> returns boolean if all elements meet condition.
        np.all(np_matrix > number) -> False
        np.all(np_matrix > number, axis=Grid.row_axis) -> [True False False False False]
    '''
    def __init__(self, **kwargs) -> None:
        self.grid = self._generate_grid(**kwargs)
        self.shape = self.grid.shape
        self.locations = np.ndindex(self.grid.shape)
        self.len = len(self.locations)

    def __repr__(self) -> str:
        return repr(self.grid)

    def __getitem__(self, key):
        return self.grid[key]

    def _generate_grid(self, **kwargs):
        if "string" in kwargs.keys():
            return Grid.from_string(**kwargs)
        return Grid.generate(**kwargs)

    def from_string(string: str, dtype, split_func=lambda row: [e for e in row]):
        '''Returns a numpy matrix from a single plain string.
        String's rows must be separated by '\n'. Callback defines row elements splitting.'''
        return np.asarray([split_func(row) for row in string.split("\n")], dtype=dtype)

    def generate(shape: tuple[int, int], fill_value: str | int | bool):
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

    def has_location(self, location: tuple[int, int]):
        return location in self.locations

    def is_in_grid(self, location: tuple[int, int]):
        return self.has_location(location)

    def invert(self):
        self.grid = ~self.grid

    def sum(self):
        '''Returns the sum of all matrix elements.'''
        return np.sum(self.grid)

    def list_index_tuples_where(result):
        '''Returns a list of index tuples for given results of numpy's where method.
        Example: get_index_tuples_where(np.where(matrix > 0))'''
        indexes = []
        for i in range(len(result[0])):
            row = result[ROW][i]
            col = result[COL][i]
            indexes.append((row, col))
        return indexes

    @property
    def neighbours_by_location(self):
        return {location: self.get_neighbours(location) for location in self.map}

    @property
    def orthogonal_neighbours_by_location(self):
        return {location: self.get_orthogonal_neighbours(location) for location in self.locations}

    def get_neighbours(self, location: tuple[int, int]):
        relative_neighbours = [
            (x, y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0) and abs(x) != abs(y)
        ]
        neighbours = [(neighbour[X] + location[X], neighbour[Y] + location[Y])
            for neighbour in relative_neighbours]
        return [neighbour for neighbour in neighbours if self.is_in_grid(neighbour)]

    def get_orthogonal_neighbours(self, location: tuple[int, int]):
        left   = list(reversed([(i, location[Y]) for i in range(location[X])]))
        top    = list(reversed([(location[X], i) for i in range(location[Y])]))
        right  = [(i, location[Y]) for i in range(*sorted([location[X] + 1, self.shape[X]]))]
        bottom = [(location[X], i) for i in range(*sorted([location[Y] + 1, self.shape[Y]]))]
        return [left, right, top, bottom]
