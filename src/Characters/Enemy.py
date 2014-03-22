# -*- coding: utf-8 -*-

from Character import Character
import pygame
from EnemyController import EnemyController
from Constants import *


class Enemy(Character):

    def __init__(self, x, y, imageName, colorkey, coordsName, numImages, player, magicNumbers=(0, 0, 0, 0, 0, 0, 0, 0), *args):
        Character.__init__(
            self, x, y, imageName, colorkey, coordsName, numImages, magicNumbers)
        self.controller = EnemyController(self, player)
        self.rect = pygame.Rect(x, y, 10, 10)
        self.atk_speed = ENEMY_ATTACK_SPEED

    def check_died(self, scene):
        if self.hp <= 0:
            scene.enemyGroup.remove(self)
