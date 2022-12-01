import numpy as np
from aoc_lib.basic.types import *


def cross_sum(*iterables, return_type=tuple):
    ''''Returns an object of the return_type with the sum of elements in the same position.
    Example: cross_sum([(1, 2), (2, 4)], list) -> [3, 6]'''
    return return_type(map(sum, zip(*iterables)))


def invert_binary(binary_str):
    '''Returns a string with the inverse of given binary string.
    Example: invert_binary("101011") -> 010100'''
    return lst_to_str(["1" if bit == "0" else "0" for bit in binary_str])


def prod(array_like_obj):
    return np.prod(array_like_obj)
