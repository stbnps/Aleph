# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

# -*- coding: utf-8 -*-

from Character import Character
from PlayerController import PlayerController
from Constants import *
import pygame

PLAYER_SPEED = 0.25
TIME_TO_ROTATE_POS = 50


class Player(Character):
    """
    Contains logic for main Player.
    """

    def __init__(self, x, y, director):
        Character.__init__(self, x, y, "player-alt.png", -1,
                           "coordPlayerAlt2.txt", [3, 3, 3, 3], magicNumbers=(-4, 10, 4, 6, -2, 4, 2, 8), director=director)

        self.controller = PlayerController(self, director)
        self.posIndex = POS_DOWN
        self.posImageIndex = 1
        self.hp = 100
        self.shield = 100
        self.shieldRegenDelay = 0
        self.atk = 20
        self.director = director
        self.mask = pygame.mask.from_surface(self.sheet.subsurface(self.sheetCoord[self.posIndex][self.posImageIndex]))

        # Better collisions this way
        self.rect.inflate_ip(-4, -6)
        self.atk_speed = PLAYER_ATTACK_SPEED

        self.selectedWpnNum = 0
        self.totalWpns = 0
        self.weapons = []

    def receive_attack(self, atk):
        """
        Reacts to an attack.
        """
        if self.shield > 0:
            self.shield -= atk
            self.shieldRegenDelay = SHIELD_REGEN_TIME

            if self.shield < 0:
                atk = -self.shield
                self.shield = 0

        # If the damage was more than the remaining shield, substract the health.
        if self.shield == 0:
            self.hp = self.hp - atk
            self.director.scene.danger = True

        print "OUCH! HP:" + str(self.hp) + " SH:" + str(self.shield)

    def check_died(self, scene):
        """
        Checks whether the Player has died.
        """
        if self.hp <= 0:
            scene.game_over()

    def setWeapons(self, weapons):
        """
        Sets player's weapons.
        """
        self.weapons = weapons
        self.totalWpns = len(weapons)
        self.setWeapon(weapons[self.selectedWpnNum])
