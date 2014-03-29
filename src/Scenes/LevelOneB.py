# -*- coding: utf-8 -*-

from Camera import *
import pygame
from Resources import *
import Constants
from LevelTwo import LevelTwo
from Level import Level
from Scenes.MessageScene import MessageScene
from Characters.Legionnaire import Legionnaire
from Characters.Caesar import Caesar



class LevelOneB(Level):

    def __init__(self, director, player):
        Level.__init__(self, director, player)
        self.player.rect.x = 381
        self.player.rect.y = 610
        self.enemyGroup.add([Legionnaire(207, 447, self.player, director),
                             Legionnaire(592, 447, self.player, director),
                             Caesar(399, 336, self.player, director)])

        self.bg = load_image("map_caesar_b_img.png", Constants.MAP_DIR)
        self.collisionBg = load_image(
            "map_caesar_b_bg.png", Constants.BG_MAP_DIR)
            
        load_music("level_one.it")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)    

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            nextLevel = LevelTwo(self.director, self.player)
            self.director.setScene(nextLevel)

        Level.processEvent(self, event)
