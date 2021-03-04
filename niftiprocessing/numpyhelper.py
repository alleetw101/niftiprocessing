import numpy as np


def normalize(array: np.array, lower: float, upper: float) -> np.array:
    newarray = array

    newarray += (0 - np.min(newarray))
    newarray *= ((upper - lower) / np.amax(newarray))
    newarray += lower

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


def rotate_image(array: np.array) -> np.array:
    return np.flip(array, axis=(0, 1))
