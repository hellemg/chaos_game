if __name__ == '__main__':
    print("Welcome to main")

    from globalConstants import *
    from canvas import *
    from colormapImage import *
    from chaosGame import *
    from colorChaosImage import *

    background = (0, 0, 0)
    use_colormap_directly = False
    # Create canvas
    try:
        canvas = Image.open('images/Canvas.png')
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
