# -*- coding: utf-8 -*-

'''
Created on 15/02/2014

@author: DaGal
'''

import pygame
import Constants
from Camera import *

from Resources import load_image
from Characters.Wolf import Wolf
from Characters.Newton import Newton
from Scenes.LevelThree import LevelThree
from Scenes.Level import Level


class LevelTwo(Level):

    def __init__(self, director, player):
        Level.__init__(self, director, player)
        self.player.rect.x = 200
        self.player.rect.y = 200
        self.enemyGroup.add([Wolf(300, 280, self.player),
                             Wolf(281, 72, self.player),
                             Wolf(422, 57, self.player),
                             Wolf(737, 160, self.player),
                             Wolf(737, 190, self.player),
                             Wolf(300, 280, self.player),
                             Wolf(500, 380, self.player),
                             Wolf(315, 495, self.player),
                             Wolf(217, 662, self.player),
                             Wolf(572, 666, self.player),
                             Wolf(917, 413, self.player),
                             Newton(896, 851, self.player)])

        self.bg = load_image("map_newton_img.png", Constants.MAP_DIR)
        self.collisionBg = load_image(
            "map_newton_bg.png", Constants.BG_MAP_DIR)

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            nextLevel = LevelThree(self.director, self.player)
            self.director.setScene(nextLevel)

        Level.processEvent(self, event)
