import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from PIL import Image

from globalConstants import *


def create_colormap():
    """
    Creates colormap from RGB-values given by COLORS
    :return: matplotlib colors ListedColormap; gradient colormap
    """
    # Size of colormap, rgba-range
    rgba_range = 256
    number_of_colors = len(COLORS)
    # Size of each gradient-color-interval
    interval_length = int(rgba_range / (number_of_colors - 1))
    # Matrix for all RGBA-colors
    colormap_pixel_values = np.ones((rgba_range, 4))
    # Gradient colors in each interval
    for i in range(number_of_colors - 1):
        for j in range(3):
            colormap_pixel_values[i * interval_length:(i + 1) * interval_length, j] = np.linspace(
                COLORS[i][j] / rgba_range, COLORS[i + 1][j] / rgba_range,
                interval_length)
    # Set colors for last entries in colormap_pixel_values (set to last colour in COLORS)
    for j in range(3):
        colormap_pixel_values[(number_of_colors - 1) * interval_length:, j] = COLORS[number_of_colors - 1][j] / rgba_range
    return ListedColormap(colormap_pixel_values)


def create_pattern(colormap, filename='ColormapImage'):
    """
    Creates a pattern by using given colormap on a function
    :param colormap: matplotlib colors ListedColormap; gradient colormap
    :param filename: string. Name of file that the image is saved to
    :return: PIL Image; pattern given by function and colormap
    """
    const = np.pi
    width = DIMS
    height = DIMS
    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)
    z = np.exp(const * y / (5 * width)) * (1 + np.sin(const * (x + y) / (height)) ** 2) + np.cos(
        const * (x + y) / height) * np.sin(const / 600 * y) * np.sin(const / 600 * x)
    plt.imsave('images/' + filename + '.png', z, cmap=colormap)
    print("...saved", filename)
    return Image.open('images/' + filename + '.png')
