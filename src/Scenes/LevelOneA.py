# -*- coding: utf-8 -*-

import Constants
import pygame
from Camera import *
from Resources import *
from EntityGroup import EntityGroup
from Level import Level
from LevelTwo import LevelTwo
from Door import Door


class LevelOneA(Level):

    def __init__(self, director, player):
        Level.__init__(self, director, player)
        self.player.rect.x = 782
        self.player.rect.y = 912
        # self.enemyGroup.add([Legionnaire(987, 768, self.player),
                                                # Legionnaire(1083, 768, self.player),
                                                # Legionnaire(1119, 768,
                                                # self.player)])

        self.door = Door(760, 570, 'door_sheet.png', -1, 'coordDoor.txt', [2])
        doorGroup = EntityGroup([])
        doorGroup.add(self.door)
        self.groups.append(doorGroup)

        self.bg = load_image("map_caesar_a_img.png", Constants.MAP_DIR)
        self.collisionBg = load_image(
            "map_caesar_a_bg.png", Constants.BG_MAP_DIR)

        load_music("level_one.it")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(loops=-1)

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            nextLevel = LevelTwo(self.director, self.player)
            self.director.setScene(nextLevel)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            self.door.setActive(True)
            # nextLevel = LevelOneB(self.director, self.player)
            # self.director.setScene(nextLevel)

        Level.processEvent(self, event)
