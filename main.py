if __name__ == '__main__':
    print("Welcome to main")

    from globalConstants import *
    from canvas import *
    from colormapImage import *
    from chaosGame import *
    from colorChaosImage import *

    background = (0, 0, 0)#(255,255,255)#(134, 67, 102)
    # Create canvas
    try:
        canvas = Image.open('images/Canvas.png')
    except:
        canvas = setup_canvas(background)

    # Create image with colormap-colors
    try:
        colormap_image = Image.open('images/ColormapImageDark.png')
    except:
        colormap = create_colormap()
        colormap_image = create_pattern(colormap)

    # Create pattern on the background
    try:
        pattern_canvas = Image.open('images/ChaosGamePattern.png')
    except:
        starting_points = setup_points()
        pattern_canvas = chaos_game(canvas, starting_points, background, filename="ChaosGameOpposite")

    # Color chaos-game
    color_chaos_image(pattern_canvas, colormap_image, background)

################################
"""
    def make_circle(c, x0, y0, r,shade):
        if r == 0:
            c[x0][y0] = shade
        else:
            for x in range(int((x0-r)), int(x0+r)):
                for y in range(int((y0-r)), int(y0+r)):
                    if ((x-x0)**2 + (y-y0)**2) <= r**2:
                        c[x][y] = shade
        return c
"""
