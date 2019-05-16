if __name__ == '__main__':
    print("Welcome to main")

    import numpy as np
    from PIL import Image
    from matplotlib import pyplot as plt

    from globalConstants import *
    from canvas import *
    from colormapImage import *
    from chaosGame import *
    from colorChaosImage import *

    # Create canvas and
    canvas = setup_canvas3D()
    points = setup_points3D()

    chaos_game(canvas, points)
    chaos_im = Image.open('ChaosImageBW_dark3.png')
    cm_im = Image.open('ColormapImageDarkNew.png')
    bg = (255, 255, 255)
    colorChaosImage(chaos_im, cm_im, bg)

    # cm_hot = create_colormap()
    # img_src = Image.open('potential.png').convert('L')
    # img_src.thumbnail((512, 512))
    # im = np.array(img_src)
    # im = cm_hot(im)
    # im = np.uint8(im * 255)
    # im = Image.fromarray(im)
    # im.save('test_hot.png')
    """
    dict = {'a':1,'b':2,'c':4}
    N = len(dict)
    vals = np.ones((20, 4))
    for i in range(N-1):
        for j in range(3):
            vals[i * N:(i + 1) * N, j] = np.linspace(dict[i][j] / P, dict[i + 1][j] / P, N)
    """
    """
    try:
        c = Image.open('CanvasDark.png')
    except:
        c = setup_canvas()

    #p = setup_points()


    create_pattern('dark')
    
    #cm_im = Image.open('ColormapImageDark.png')
    cm_im = Image.open('yolo.png')

    width, height = cm_im.size
    width = 3.5*height
    #chaos_game(c, p, cm_im)
    c = Image.open('chaosImageDarkBW.png')

    area = (1000-width/2, 1000-height/2, 1000+width/2, 1000+height/2) #left, up, right, bottom
    c = c.crop(area)

    colorChaosImage(c, cm_im, (0, 57, 67))

    c.show()

    """
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
