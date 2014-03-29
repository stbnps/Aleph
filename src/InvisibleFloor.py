# -*- coding: utf-8 -*-

from Entity import Entity
import pygame
from Constants import *
import os
from Scenes.MessageScene import MessageScene
from Resources import load_sound

class InvisibleFloor(Entity):
    def __init__(self, x, y, w, h, imageName=None, colorkey=None, coordsName=None, numImages=None, *args):
        Entity.__init__(self, x, y, imageName, colorkey, coordsName, numImages)
        self.rect = pygame.Rect(x,y,w,h)    
    
    def draw (self, time, camera):
        pass
