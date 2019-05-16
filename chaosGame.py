from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

from globalConstants import *


def chaos_game(canvas, points, mode='dark', cm_im=None):
    """
    Creates pattern by chaos game algorithm
    :param canvas: PIL Image; empty canvas to fill with chaos-pattern
    :param points: Numpy array; points that give position of vertices
    :param cm_im: PIL Image; color to add to chaos-pattern
    :return:
    """
    # Set starting vertex
    nr_of_points = points.shape[0]
    filename = 'ChaosImageBW_' + mode + str(nr_of_points)
    current_point = points[0]
    current_x = DIMS / 3
    current_y = DIMS / 3
    for n in range(N):
        if (n % 1000 == 0):
            print("round: ", n)
        next_point = points[np.random.randint(nr_of_points)]
        if nr_of_points == 5:
            if (next_point[0] != current_point[0]) and (next_point[1] != current_point[1]):
                current_x = int((current_x + next_point[0]) / 2)
                current_y = int((current_y + next_point[1]) / 2)
                current_point = next_point
                # pixel = cm_im.getpixel((current_x, current_y))
                pixel = 0
                canvas.putpixel((current_x, current_y), pixel)
        elif nr_of_points != 5:
            current_x = int((current_x + next_point[0]) / 2)
            current_y = int((current_y + next_point[1]) / 2)
            current_point = next_point
            # pixel = cm_im.getpixel((current_x, current_y))
            pixel = 0
            canvas.putpixel((current_x, current_y), pixel)
    canvas.save(filename+'.png')
    print('Saved', filename+'.png')
    #plt.imsave(filename, canvas)
    # return canvas
