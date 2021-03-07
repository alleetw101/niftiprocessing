import numpy as np


def normalize(array: np.array, lower: float, upper: float) -> np.array:
    """Normalizes array

    Normalizes input array into values between two values. Values are set in arguments as lower and upper.

    Args:
        array: A numpy array containing data points for normalization.
        lower: An int for the lower bound of normalization.
        upper: An int for the upper bound of normalization.
    Returns:
        A numpy array with normalized values between lower and upper.
    """
    newarray = array

    newarray += (0 - np.min(newarray))
    newarray *= ((upper - lower) / np.amax(newarray))
    newarray += lower

    return newarray


def denoise(array: np.array, lower=None, upper=None) -> np.array:
    """Denoising

    Removes outlier values from array. Cutoff range is specified with lower and upper as bounds. Values are
    repalced with 0..

    Args:
        array: A numpy array containing data points for denoising.
        lower: An int for the lower bound of removal.
        upper: An int for the upper bound of removal.
    Returns:
        A numpy array with values lower than 'lower' and higher than 'upper' replaced with 0..
    """
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
