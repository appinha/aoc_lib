import numpy as np
from aoc_lib.basic.types import list_to_str


def invert_binary(binary_str):
    """Returns a string with the inverse of given binary string.
    Example: invert_binary("101011") -> 010100"""
    return list_to_str(["1" if bit == "0" else "0" for bit in binary_str])


def prod(array_like_obj):
    return np.prod(array_like_obj)
