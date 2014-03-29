# -*- coding: utf-8 -*-

from Resources import load_image
from Entity import Entity
import pygame
from Constants import *
import os

class Laser(Entity):
    def __init__(self, x, y, imageName=None,colorkey=None, coordsName=None, numImages=None, *args):
        Entity.__init__(self, x, y, imageName, colorkey, coordsName,numImages)      
        self.active = True      
        self.mask = pygame.mask.from_surface(self.sheet, 240)
        self.name = imageName
        
    def setActive(self, active):
        self.active = active
    
    def draw(self, screen, camera):
        if self.active:
            Entity.draw(self, screen, camera)
            
