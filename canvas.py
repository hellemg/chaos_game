import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from globalConstants import *


def setup_canvas(mode='dark'):
    """

    :param mode:
    :return:
    """
    if mode == 'dark':
        bg = (0, 57, 67)
        filename = 'CanvasDark.png'
    else:
        bg = (0, 101, 129)
        filename = 'CanvasMedium.png'
    canvas = np.ones((DIMS, DIMS))
    canvas = Image.fromarray(canvas).convert("RGB")
    for r in range(DIMS):
        for c in range(DIMS):
            canvas.putpixel((r, c), bg)
    plt.imsave(filename, canvas)
    return canvas


def setup_points(nr_of_points=5):
    # Create starting points
    points_array = np.ones((5, 2))
    radius = DIMS / 2
    theta = 2 * np.pi / nr_of_points
    for i in range(nr_of_points):
        x = radius * np.cos(theta * i) + DIMS / 2
        y = radius * np.sin(theta * i) + DIMS / 2
        # To draw the points (make_circle is currently commented out)
        # canvas = make_circle(canvas, x, y, 20, 150)
        points_array[i] = x, y
    return points_array


def setup_canvas3D(mode='dark'):
    # Large canvas
    if mode == 'dark':
        bg = (255, 255, 255)
        filename = 'CanvasDark.png'
    else:
        bg = (0, 101, 129)
        filename = 'CanvasMedium.png'
    canvas = np.ones((DIMS, DIMS))
    canvas = Image.fromarray(canvas).convert("RGB")
    for r in range(DIMS):
        for c in range(DIMS):
            canvas.putpixel((r, c), bg)
    plt.imsave(filename, canvas)
    return canvas


def setup_points3D(nr_of_points=3):
    # Create starting points
    points_array = np.ones((nr_of_points, 2))
    radius = DIMS / 2
    theta = 2 * np.pi / nr_of_points
    for i in range(nr_of_points):
        x = radius * np.cos(theta * i) + DIMS / 2
        y = radius * np.sin(theta * i) + DIMS / 2
        # To draw the points (make_circle is currently commented out)
        # canvas = make_circle(canvas, x, y, 20, 150)
        points_array[i] = x, y
    return points_array
