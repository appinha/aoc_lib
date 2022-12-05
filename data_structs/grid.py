import numpy as np


def np_generate(shape: tuple, fill_value: str):
    if fill_value == True:
        return np.ones(shape, dtype=bool)
    elif fill_value == False:
        return np.zeros(shape, dtype=bool)
    elif fill_value.isdigit():
        return np.full(shape, fill_value, dtype=int)
    else:
        return np.full(shape, fill_value)


def np_invert(grid: np.ndarray):
    return ~grid
