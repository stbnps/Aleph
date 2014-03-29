# -*- coding: utf-8 -*-

from Character import Character
import pygame
from EnemyController import EnemyController
from Constants import *


class Enemy(Character):
    """
    Contains logic for all kinds of enemies.
    """

    def __init__(self, x, y, imageName, colorkey, coordsName, numImages, player, director, magicNumbers=(0, 0, 0, 0, 0, 0, 0, 0), *args):        
        Character.__init__(self, x, y, imageName, colorkey, coordsName, numImages, director, magicNumbers)
        self.controller = EnemyController(self, player, director)
        self.rect = pygame.Rect(x, y, 10, 10)
        self.atk_speed = ENEMY_ATTACK_SPEED

    def check_died(self, scene):
        """
        Check whether the enemy has died.
        """
        if self.hp <= 0:
            scene.enemyGroup.remove(self)
