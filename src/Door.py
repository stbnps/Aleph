# -*- coding: utf-8 -*-

import pygame
import os
from Entity import Entity
from Constants import *
from Resources import load_sound

class Door(Entity):
    def __init__(self, x, y, imageName=None, colorkey=None, coordsName=None, numImages=None, sound = None, soundVolume = 1, *args):
        Entity.__init__(self, x, y, imageName, colorkey, coordsName, numImages)
        self.active = False
        self.posIndex = POS_UP
        self.posImageIndex = 0  
        
        if sound:
            self.sound = load_sound(sound)
            self.sound.set_volume(soundVolume)
        else:
            self.sound = None   
        
    def setActive(self, active):
        self.active = active
        self.playSound()
        
    def playSound(self):
        if self.sound:
            self.sound.play()

    def stopSound(self):
        if self.sound:
            self.sound.stop()
        
    def update(self, time, scene):        
            
        if self.active:
            self.posImageIndex = 1  
        
        
        
