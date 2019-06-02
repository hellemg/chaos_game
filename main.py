if __name__ == '__main__':
    print("Welcome to main")

    from globalConstants import *
    from canvas import *
    from colormapImage import *
    from chaosGame import *
    from colorChaosImage import *
    from matplotlib import cm

    background = (255, 255, 255)
    use_colormap_directly = True
    # Create canvas
    try:
        canvas = Image.open('images/CanvasLight.png')
    except:
        canvas = setup_canvas(background)

    # Create image with colormap-colors
    try:
        colormap_image = Image.open('images/ColormapImage.png')
    except:
        colormap = create_colormap()
        colormap_image = create_pattern(colormap)

    # Create pattern on the background
    try:
        pattern_canvas = Image.open('images/ChaosGamePattern.png')
        color_chaos_image(pattern_canvas, colormap_image, background)
    except:
        starting_points = setup_points()
        if use_colormap_directly:
            chaos_game(canvas, starting_points, background, filename='ChaosGamePattern', colormap_image=colormap_image)
        else:
            pattern_canvas = chaos_game(canvas, starting_points, background)
            color_chaos_image(pattern_canvas, colormap_image, background)
    """

    def plot_color_gradients(cmap_list):
        gradient = np.linspace(0, 1, 256)
        gradient = np.vstack((gradient, gradient))
        plt.imshow(gradient, aspect='auto', cmap=cmap_list)
        plt.show()


    cmap_list=create_colormap()
    plot_color_gradients(cmap_list)
    """