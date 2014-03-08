# -*- coding: utf-8 -*-

from Character import Character
import pygame
from EnemyController import EnemyController

class Enemy(Character):
	def __init__(self, x, y, imageName, colorkey, coordsName, numImages, player, *args):
		Character.__init__(self, x, y, imageName, colorkey, coordsName, numImages)
		self.controller = EnemyController(self, player)
		self.rect = pygame.Rect(x, y, 10, 10)