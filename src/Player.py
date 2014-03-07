# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

# -*- coding: utf-8 -*-

from Character import Character
import pygame
import Util

PLAYER_SPEED = 0.25
TIME_TO_ROTATE_POS = 50

POS_UP = 0
POS_RIGHT = 1
POS_DOWN = 2
POS_LEFT = 3
POS_NUM = 4

class Player(Character):
	def __init__(self, x, y, imageName, colorkey, coordsName, numImages, *args):
		Character.__init__(self, x, y, imageName, colorkey, coordsName, numImages)

		self.posIndex = POS_DOWN
		self.posImageIndex = 1

		# Better collisions this way
		self.rect.inflate_ip(-4, -6)

	def update(self, time, collisionMap):
		keys = pygame.key.get_pressed()
		self.speedX = 0
		self.speedY = 0

		# Hector, please merge this shit with the controller asap:
		if keys[pygame.K_a]:
			self.speedX = -PLAYER_SPEED
			self.posIndex = POS_LEFT
		elif keys[pygame.K_d]:
			self.speedX = PLAYER_SPEED
			self.posIndex = POS_RIGHT
		if keys[pygame.K_s]:
			self.speedY = PLAYER_SPEED
			self.posIndex = POS_DOWN
		elif keys[pygame.K_w]:
			self.speedY = -PLAYER_SPEED
			self.posIndex = POS_UP

		if (self.speedX != 0) or (self.speedY != 0):
			self.rotatePosImage(time)

		self.move(time, collisionMap)
