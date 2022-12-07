import collections
import numpy as np
from aoc_lib.basic.numbers import *
from aoc_lib.basic.types import *


X = 0
Y = 1
Z = 2

ROW = 0
COL = 1


class HashGrid():
    def from_string(string: str, type, split_func=lambda row: row.split()):
        '''Returns a hashmap from a single plain string.
        String's rows must be separated by '\n'. split_func defines row elements splitting.'''
        hashmap = collections.defaultdict(type)
        for y, line in enumerate(string.split("\n")):
            for x, value in enumerate(split_func(line)):
                hashmap[(x, y)] = type(value)
        return hashmap

    def shape(hashmap: dict):
        return cross_sum(max(hashmap.keys()), (1, 1))


class NumpyGrid():
    '''Examples of useful numpy methods:
        np.where(condition) -> returns indexes where condition is met.
        np.where(np_matrix == number) -> [[i1_row, i2_row], [i1_col, i2_col]]

        np.any(condition) -> returns boolean if any element meets condition.
        np.all(condition) -> returns boolean if all elements meet condition.
        np.all(np_matrix > number) -> False
        np.all(np_matrix > number, axis=Grid.row_axis) -> [True False False False False]
    '''

    def from_string(string: str, type, split_func=lambda row: row.split()):
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

    def has_position(pos: tuple[int, int], shape: tuple[int, int]):
        return (0 <= pos[ROW] < shape[ROW]) and (0 <= pos[COL] < shape[COL])

    def invert(grid: np.ndarray):
        return ~grid

    def sum(grid: np.ndarray):
        '''Returns the sum of all matrix elements.'''
        return np.sum(grid)

    def list_index_tuples_where(result):
        '''Returns a list of index tuples for given results of numpy's where method.
        Example: get_index_tuples_where(np.where(matrix > 0))'''
        indexes = []
        for i in range(len(result[0])):
            row = result[ROW][i]
            col = result[COL][i]
            indexes.append((row, col))
        return indexes
