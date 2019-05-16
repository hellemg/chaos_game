from matplotlib import pyplot as plt


def check_if_bg_pixel(pixel, bg):
    """
    Checks if a pixel contains the given background-color
    :param pixel: tuple (4 values, RGBA)
    :param bg: tuple, (3 values, RGB)
    :return: boolean
    """
    return (pixel[0] == bg[0]) and (pixel[1] == bg[1]) and (pixel[2] == bg[2])


def colorChaosImage(chaos_im, cm_im, bg):
    """
    Colors non-background part of image
    :param chaos_im: PIL Image, white chaos-pattern on bg-colored pattern
    :param cm_im: PIL Image, color-pattern to merge with chaos-pattern
    :param bg: tuple, (3 values, RGB) background-color of chaos_im
    :return: NONE, saves created image
    """
    filename = 'ColoredChaosGameBW_dark3'
    width, height = chaos_im.size
    for h in range(height):
        for w in range(width):
            pixel = chaos_im.getpixel((w, h))
            if not check_if_bg_pixel(pixel, bg):
                chaos_im.putpixel((w, h),(204, 102, 51))
                #chaos_im.putpixel((w, h), cm_im.getpixel((w, h)))
    plt.imsave(filename + '.png', chaos_im)
