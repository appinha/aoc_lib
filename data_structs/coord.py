from aoc_lib.basic.regex import find_all_integers
from typing import NamedTuple
import re


class Coord2D(NamedTuple):
    x: int
    y: int

    @property
    def row(self):
        return self.x

    @property
    def col(self):
        return self.y

    @property
    def as_list(self):
        return [self.x, self.y]

    @property
    def as_tuple(self):
        return (self.x, self.y)


def string_to_tuple(string: str):
    return tuple(find_all_integers(string))


def string_to_coord2D(string: str):
    return Coord2D(*find_all_integers(string))


def find_all_coords(string, return_type=tuple):
    '''Given a string containing comma separated integers, returns a list of coordinates.
    Example: find_all_coords("-1,4 > 2,-6 > 10,6") -> [(-1,4), (2,-6), (10,6)]'''

    def process_substring(substring):
        if return_type == Coord2D:
            return string_to_coord2D(substring)
        return string_to_tuple(substring)

    return list(map(process_substring, re.findall(r'[0-9\-,]+', string)))


def cross_sum(*coords, return_type=tuple):
    '''Returns an object of the return_type with the sum of elements in the same position.
    Example: cross_sum([(1, 2), (2, 4)], list) -> [3, 6]'''
    return return_type(map(sum, zip(*coords)))


def find_limits(coords):
    '''Returns two lists with the minimums and maximums of each position of coords.
    Example: find_limits([(1, 2), (2, 4), (3, 3)]) -> [1, 2], [3, 4]
    Usage: (min_x, min_y), (max_x, max_y) = find_limits(list_of_tuples)'''
    return list(map(min, zip(*coords))), list(map(max, zip(*coords)))
