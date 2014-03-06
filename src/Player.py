# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

# -*- coding: utf-8 -*-

from Character import Character
import pygame
from Constants import DOWN, UP, LEFT, RIGHT

PLAYER_SPEED = 0.25


class Player(Character):
	def __init__(self, x, y, *args):
		Character.__init__(self, x, y)
		self.rect = pygame.Rect(x, y, 10, 10)

	def update(self, time, collisionMap):
		keys = pygame.key.get_pressed()
		self.speedX = 0
		self.speedY = 0

		if keys[DOWN]:
			self.speedY = PLAYER_SPEED
		elif keys[UP]:
			self.speedY = -PLAYER_SPEED
		if keys[LEFT]:
			self.speedX = -PLAYER_SPEED
		elif keys[RIGHT]:
			self.speedX = PLAYER_SPEED

		self.move(time, collisionMap)
