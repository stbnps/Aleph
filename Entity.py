# -*- coding: utf-8 -*-

from pygame.sprite import *

class Entity(Sprite):
    def __init__(self, x, y, *args):
        Sprite.__init__(self)
        self.rect = Rect(x, y, 0, 0)

    def update(self, time, *args):
        pass

    def draw(self, screen, camera):
    # Fix this shit when we have actual sprites!
        pygame.draw.rect(screen, 0xFFFFFF, camera.apply(self))
