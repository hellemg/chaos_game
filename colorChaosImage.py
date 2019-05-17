from matplotlib import pyplot as plt


def check_if_bg_pixel(pixel, background):
    """
    Checks if a pixel contains the given background-color
    :param pixel: tuple, 1 x 4
    :param background: tuple, 1 x 3
    :return: boolean; True if pixel is the same RGB-color as background
    """
    return (pixel[0] == background[0]) and (pixel[1] == background[1]) and (pixel[2] == background[2])


def color_chaos_image(chaos_image, colormap_image, background, filename = 'ChaosGameColored'):
    """
    Colors patterned part
    :param chaos_image: PIL Image, DIMS x DIMS; white chaos-pattern on bg-colored pattern
    :param colormap_image: PIL Image, DIMS x DIMS; color-pattern to merge with chaos-pattern
    :param background: tuple, (3 values, RGB) background-color of chaos_im
    filename: string. Name of file that the image is saved to
    :return: PIL Image; colored pattern
    """
    width, height = chaos_image.size
    for h in range(height):
        for w in range(width):
            pixel = chaos_image.getpixel((w, h))
            if not check_if_bg_pixel(pixel, background):
                new_pixel=colormap_image.getpixel((w,h))
                chaos_image.putpixel((w, h),new_pixel)
    plt.imsave('images/'+filename + '.png', chaos_image)
    return chaos_image
