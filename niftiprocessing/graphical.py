import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    print('For external plotting, matplotlib>=3.0 must be installed')


def plot_slice(data_array: np.ndarray, slice_index: int, time_index: int = 0, step_size: int = 10, figsize=(10, 9),
               vplots: int = 1, hplots: int = 1, cmap: str = 'gray'):
    """Plot MRI/fMRI slice(s) in matplotlib

    Plot image(s) of MRI/fMRI slice(s) in matplotlib

    Args:
        data_array: A numpy array containing data points for an MRI/fMRI scan
        slice_index: An integer specifying index of slice to plot
        time_index: Optional; An integer specifying time index ([0]) of slice to plot in fMRI data arrays
        step_size: Optional; An integer specyfying number of indices to skip in data array when plotting two or more
            slices
        figsize: Optional; A tuple specyfing matplotlib figure size
        vplots: Optional; An integer specyfying number of vertical plots in matplotlib figure
        hplots: Optional; An integer specyfying number of horizontal plots in matplotlib figure
        cmap: Optional; A string specifying matplotlib plot cmap(s)
    """
    plt.figure(figsize=figsize)

    if data_array.ndim == 3 or (data_array.ndim == 4 and data_array.shape[-1] <= 3):
        for position in range(vplots * hplots):
            plt.subplot(vplots, hplots, position + 1)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(data_array[slice_index + (position * step_size)], cmap=cmap)
            plt.title(f'Slice index: {slice_index + (position * step_size)}')
    elif data_array.ndim == 4 or data_array.ndim == 5:
        for position in range(vplots * hplots):
            plt.subplot(vplots, hplots, position + 1)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(data_array[time_index][slice_index + (position * step_size)], cmap=cmap)
            plt.title(f'Time index: {time_index}, Slice index: {slice_index + (position * step_size)}')
    else:
        raise ValueError('Input data must be a 3d, 4d, or 5d image')

    plt.show()