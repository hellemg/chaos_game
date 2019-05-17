import numpy as np

from globalConstants import *


def chaos_game(canvas, points, bg=(0, 57, 67), filename='ChaosGame.png', colormap_image=None):
    """
    Creates pattern by chaos game algorithm
    :param canvas: PIL Image; empty canvas to fill with chaos-pattern
    :param points: Numpy array; points that give position of vertices
    :param bg: tuple, 1x3. Backgroundcolor for the canvas
    :param filename: string. Name of file that the image is saved to
    :param colormap_image: PIL Image; colored image to overlay pattern
    :return: PIL Image, DIMS x DIMS; Image with colored chaos pattern
    """
    # Set initial conditions
    nr_of_points = points.shape[0]
    current_point = points[0]
    current_x = DIMS / 3
    current_y = DIMS / 3
    for n in range(N):
        if (n % 1000 == 0):
            print("round: ", n)
        next_point = points[np.random.randint(nr_of_points)]
        # Run chaos algorithm for 5 starting points
        if nr_of_points == 5:
            if (next_point[0] != current_point[0]) and (next_point[1] != current_point[1]):
                current_x = int((current_x + next_point[0]) / 2)
                current_y = int((current_y + next_point[1]) / 2)
                current_point = next_point
                pixel = colormap_image.getpixel((current_x, current_y))
                canvas.putpixel((current_x, current_y), pixel)
        # Run chaos algorithm for 3 starting points
        elif nr_of_points == 3:
            current_x = int((current_x + next_point[0]) / 2)
            current_y = int((current_y + next_point[1]) / 2)
            current_point = next_point
            pixel = colormap_image.getpixel((current_x, current_y))
            canvas.putpixel((current_x, current_y), pixel)
    canvas.save(filename)
    print('..saved', filename)
    return canvas
