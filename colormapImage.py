import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from PIL import Image

from globalConstants import *

# Create list of tuples with RGB-values for each colour in colourmap
COLORS = [(243, 188, 147),  # Yellow
          (255, 129, 130),  # Light orange
          (236, 109, 128),  # Dark orange
          (178, 85, 114),  # Red
          (134, 67, 102),  # Dark red
          (21, 37, 60),  # Blue-black
          (0, 57, 67),  # Dark blue
          (0, 101, 129),  # Medium blue
          (121, 178, 205)]  # Light blue

colors_dict = {'Yellow': (243, 188, 147), 'Light orange': (255, 129, 130), 'Dark orange': (236, 109, 128),
               'Red': (178, 85, 114), 'Dark red': (134, 67, 102), 'Blue-black': (21, 37, 60), 'Dark blue': (0, 57, 67),
               'Medium blue': (0, 101, 129), 'Light blue': (121, 178, 205)}

# Define RGB-size, size of intervals, and size of colormap
P = 256


def create_colormap():
    """
    Creates colormap from RGB-values given by COLORS
    :param colors: list of tuples (3 values, RGB)
    :return: TYPE????, colormap where first values in colors are lightest/darkest??
    """
    num_colours = len(COLORS)
    # interval-length must be 1 less than the number of colours
    num_values = int(P / (num_colours - 1))
    #define matrix for P x RGBA values
    vals = np.ones((P, 4))
    # Set colours to gradient to next neighbour
    for i in range(num_colours - 1):
        for j in range(3):
            vals[i * num_values:(i + 1) * num_values, j] = np.linspace(COLORS[i][j] / P, COLORS[i + 1][j] / P,
                                                                       num_values)
    # Ensure that values at the end has a colour (here set to last colour)
    for j in range(3):
        vals[8 * num_values:, j] = COLORS[num_colours - 1][j] / P
    return ListedColormap(vals)


def create_pattern(mode='dark', cmap=create_colormap()):
    # pop_number = make_a_color_dict[mode]
    if mode == 'dark':
        COLORS.pop(6)
        filename = 'ColormapImageDark.png'
    else:
        COLORS.pop(7)
        filename = 'ColormapImageMedium.png'
    const = np.pi
    # These parameters for the functions currently work, if these are changed the function must be changes (nightmare)
    width = DIMS
    height = DIMS / 4
    # x = np.arange(width)
    # y = np.arange(height)
    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)
    """
    z = np.exp((2 * y + x) / width) * (np.sin(0.5 * const * (x) / (height))) + (
        np.cos(const * 2 * y / height)) + np.cos(const * (x + y) / height)
    """
    # z = e ^ y * sin ^ 2(x) + y * cos ^ 2(y)
    #######
    ########FIND THE ONE IN yolo.png############
    z = np.exp(const * y / (2 * width)) * (1 + np.sin(const * (x + y) / (height)) ** 2) + y / height * (
        np.cos(const * y / height)) ** 2 + np.cos(
        const * (x + y) / height)

    plt.imsave(filename, z, cmap=cmap)
