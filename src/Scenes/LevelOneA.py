# -*- coding: utf-8 -*-

import Constants
import pygame
from Camera import *
from Resources import *
from EntityGroup import EntityGroup
from Level import Level
from LevelTwo import LevelTwo
from LevelOneB import LevelOneB
from Door import Door
from Scenes.MessageScene import MessageScene
from Characters.Legionnaire import Legionnaire
from Characters.Centurion import Centurion
from Weapons.WpnBlade import WpnBlade
from Weapons.WpnBow import WpnBow


class LevelOneA(Level):

    def __init__(self, director, player):
        Level.__init__(self, director, player)
        self.player.rect.x = 782
        self.player.rect.y = 912
        self.dead_sub_boss = 0      #Counts the dead Centurions.
        self.enemyGroup.add([Legionnaire(987, 768, self.player, director),
                             Legionnaire(1083, 768, self.player, director),
                             Legionnaire(1119, 768, self.player, director),
                             Legionnaire(987, 834, self.player, director),
                             Legionnaire(477, 747, self.player, director),
                             Legionnaire(645, 738, self.player, director),
                             Legionnaire(477, 891, self.player, director),
                             Legionnaire(645, 788, self.player, director),
                             Centurion(150, 288, self.player, director),
                             Centurion(1455, 288, self.player, director),
                             Centurion(1329, 1248, self.player, director)]) 

        self.door = Door(760, 575, 'door_sheet.png', -1, 'coordDoor.txt', [2], 'door_open.wav')     
        self.doorGroup = EntityGroup([])
        self.doorGroup.add(self.door)
        self.groups.append(self.doorGroup)

        self.bg = load_image("map_caesar_a_img.png", Constants.MAP_DIR)
        self.collisionBg = load_image(
            "map_caesar_a_bg.png", Constants.BG_MAP_DIR)

        load_music("level_one.it")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

        player.setWeapons([WpnBlade("wpns2.png", -1, pygame.Rect(344, 342, 28, 28), "blade_swing.wav", 0.5), \
                          WpnBow("items-1.png", None, pygame.Rect(0, 24, 24, 24))])

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            nextLevel = LevelTwo(self.director, self.player)
            self.director.setScene(nextLevel)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            self.door.setActive(True)
            # nextLevel = LevelOneB(self.director, self.player)
            # self.director.setScene(nextLevel)

        Level.processEvent(self, event)
    
    def update(self, time):
        Level.update(self, time)
        if not self.door.active and self.dead_sub_boss == 3:
            #When all Centurions are dead we open the door
            self.door.setActive(True)
        if len(pygame.sprite.spritecollide(self.player,self.doorGroup,False)) == 1: 
            if self.door.active == False:
                m = MessageScene(self.director, self, 'Warning', 'You shall not pass!', 'Press to continue')
                self.director.setScene(m)
                self.player.rect.y+=25
            if self.door.active == True:
                nextLevel = LevelOneB(self.director, self.player)
                self.director.setScene(nextLevel)    
