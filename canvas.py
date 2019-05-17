import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from globalConstants import *


def setup_canvas(background=(0, 57, 67), filename='Canvas.png'):
    """
    Creates an empty canvas
    :param background: tuple, 1 x 3; Backgroundcolor for the canvas
    :param filename: string; Name of file that the canvas is saved to
    :return: PIL Image, DIMS x DIMS
    """
    canvas = np.ones((DIMS, DIMS))
    canvas = Image.fromarray(canvas).convert("RGB")
    for r in range(DIMS):
        for c in range(DIMS):
            canvas.putpixel((r, c), background)
    plt.imsave(filename+'png', canvas)
    print('..saved', filename)
    return canvas


def setup_points(nr_of_starting_points=5):
    """
    Adds evenly distributed starting points to canvas
    :param nr_of_points: int; Number of points to add
    :return: numpy array, nr_of_points x 2; Contains coordinates for the starting points
    """
    points_array = np.ones((nr_of_starting_points, 2))
    radius = DIMS / 2
    theta = 2 * np.pi / nr_of_starting_points
    for i in range(nr_of_starting_points):
        x = radius * np.cos(theta * i) + DIMS / 2
        y = radius * np.sin(theta * i) + DIMS / 2
        points_array[i] = x, y
    print('..calculated coordinates for starting points')
    return points_array
