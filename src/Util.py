
import pygame
import os

import Constants

def load_image(name, colorkey=None):
    fullname = os.path.join(Constants.IMAGE_DIR , name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    
    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    else:
        image = image.convert_alpha()
    return image