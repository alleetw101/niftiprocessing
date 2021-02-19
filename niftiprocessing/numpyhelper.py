import numpy as np


def normalize(array: np.array, value_range=(0., 1.)) -> np.array:
    newarray = array

    newarray += (0 - np.min(newarray))
    newarray *= ((value_range[1] - value_range[0]) / np.amax(newarray))

    return newarray


def denoise(array: np.array, lower=None, upper=None) -> np.array:
    newarray = array

    if lower:
        newarray[newarray < lower] = lower
        if upper:
            newarray[newarray > upper] = lower
    elif upper:
        newarray[newarray > upper] = 0.

    return newarray


def pad(array: np.array, shape: (int, int, int)) -> np.array:
    newarray = array

    for array_d, output_d in zip(newarray.shape, shape):
        if array_d > output_d:
            raise ValueError('Desired dimensions must be greater than input dimensions')

