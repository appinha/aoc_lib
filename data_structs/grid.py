import collections
import numpy as np
from pprint import pprint
from aoc_lib.basic.numbers import *
from aoc_lib.basic.types import *


X = 0
Y = 1
Z = 2

ROW = 0
COL = 1


class HashGrid():
    def __init__(self, string: str, type, split_func=lambda row: row) -> None:
        self.map = HashGrid.from_string(string, type, split_func)
        self.len = len(self.map)

    def __repr__(self) -> str:
        pprint(self.map)
        return ""

    def __getitem__(self, key):
        return self.map[key]

    def from_string(string: str, type, split_func=lambda row: row):
        '''Returns a hashmap from a single plain string.
        String's rows must be delimited by '\n'. split_func defines how row elements are split.'''
        hashmap = collections.defaultdict(type)
        for y, line in enumerate(string.split("\n")):
            for x, value in enumerate(split_func(line)):
                hashmap[(x, y)] = type(value)
        return hashmap

    @property
    def shape(self):
        return cross_sum(max(self.map.keys()), (1, 1))

    @property
    def immediate_adjacencies_by_pos(self):
        return {pos: self.get_immediate_adjacencies(pos) for pos in self.map}

    @property
    def orthogonal_adjacencies_by_pos(self):
        return {pos: self.get_orthogonal_adjacencies(pos) for pos in self.map}

    def is_in_map(self, pos: tuple[int, int]):
        return (0 <= pos[X] < self.shape[X]) and (0 <= pos[Y] < self.shape[Y])

    def get_immediate_adjacencies(self, pos: tuple[int, int]):
        relative_adjs = [
            (x, y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0) and abs(x) != abs(y)
        ]
        absolute_adjs = [(adj[X] + pos[X], adj[Y] + pos[Y]) for adj in relative_adjs]
        return [adj for adj in absolute_adjs if self.is_in_map(adj)]

    def get_orthogonal_adjacencies(self, pos: tuple[int, int]):
        left   = list(reversed([(i, pos[Y]) for i in range(pos[X])]))
        top    = list(reversed([(pos[X], i) for i in range(pos[Y])]))
        right  = [(i, pos[Y]) for i in range(*sorted([pos[X] + 1, self.shape[X]]))]
        bottom = [(pos[X], i) for i in range(*sorted([pos[Y] + 1, self.shape[Y]]))]
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
        self.positions = np.ndindex(self.grid.shape)
        self.len = np.prod(self.shape)

    def __repr__(self) -> str:
        print(self.grid)
        return ""

    def __getitem__(self, key):
        return self.grid[key]

    def _generate_grid(self, **kwargs):
        if "string" in kwargs.keys():
            return Grid.from_string(**kwargs)
        return Grid.generate(**kwargs)

    def from_string(string: str, type, split_func=lambda row: [e for e in row]):
        '''Returns a numpy matrix from a single plain string.
        String's rows must be separated by '\n'. Callback defines row elements splitting.'''
        return np.asarray([split_func(row) for row in string.split("\n")], dtype=type)

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

    def has_position(self, pos: tuple[int, int]):
        return (0 <= pos[ROW] < self.shape[ROW]) and (0 <= pos[COL] < self.shape[COL])

    def invert(self):
        self.grid = ~self.grid

    def sum(self):
        '''Returns the sum of all matrix elements.'''
        return np.sum(self.grid)

    @property
    def orthogonal_adjacencies_by_pos(self):
        return {pos: self.get_orthogonal_adjacencies(pos) for pos in self.positions}

    def get_orthogonal_adjacencies(self, pos: tuple[int, int]):
        left   = list(reversed([(i, pos[Y]) for i in range(pos[X])]))
        top    = list(reversed([(pos[X], i) for i in range(pos[Y])]))
        right  = [(i, pos[Y]) for i in range(*sorted([pos[X] + 1, self.shape[X]]))]
        bottom = [(pos[X], i) for i in range(*sorted([pos[Y] + 1, self.shape[Y]]))]
        return [left, right, top, bottom]

    def list_index_tuples_where(result):
        '''Returns a list of index tuples for given results of numpy's where method.
        Example: get_index_tuples_where(np.where(matrix > 0))'''
        indexes = []
        for i in range(len(result[0])):
            row = result[ROW][i]
            col = result[COL][i]
            indexes.append((row, col))
        return indexes
