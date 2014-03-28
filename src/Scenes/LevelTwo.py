# -*- coding: utf-8 -*-

'''
Created on 15/02/2014

@author: DaGal
'''

import pygame
import Constants
from Camera import *

from Resources import *
from Characters.Wolf import Wolf
from Characters.Newton import Newton
from Scenes.LevelThree import LevelThree
from Scenes.Level import Level
from Weapons.WpnBlade import WpnBlade
from Weapons.WpnRifle import WpnRifle



class LevelTwo(Level):

    def __init__(self, director, player):
        Level.__init__(self, director, player)
        self.player.rect.x = 200
        self.player.rect.y = 200
        self.enemyGroup.add([Wolf(300, 280, self.player, director),
                             Wolf(281, 72, self.player, director),
                             Wolf(422, 57, self.player, director),
                             Wolf(737, 160, self.player, director),
                             Wolf(737, 190, self.player, director),
                             Wolf(300, 280, self.player, director),
                             Wolf(500, 380, self.player, director),
                             Wolf(315, 495, self.player, director),
                             Wolf(217, 662, self.player, director),
                             Wolf(572, 666, self.player, director),
                             Wolf(917, 413, self.player, director),
                             Newton(896, 851, self.player, director)])

        self.bg = load_image("map_newton_img.png", Constants.MAP_DIR)
        self.collisionBg = load_image(
            "map_newton_bg.png", Constants.BG_MAP_DIR)

        load_music("level_two.s3m")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        player.setWeapons([WpnBlade("wpns2.png", -1, pygame.Rect(440, 278, 26, 26), "blade_swing.wav", 0.5), \
                          WpnRifle()])

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            nextLevel = LevelThree(self.director, self.player)
            self.director.setScene(nextLevel)

        Level.processEvent(self, event)
