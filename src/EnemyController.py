# -*- coding: utf-8 -*-

import pygame
from Controller import Controller
from Constants import *
import math
import random

class EnemyController(Controller):

	def __init__(self, enemy, player):
		Controller.__init__(self, enemy)
		self.player = player
		self.enemy_speed = 0.10

	def update(self, time, collisionMap):
		keys = pygame.key.get_pressed()
		self.character.speedX = 0
		self.character.speedY = 0

		a = self.player.rect.x - self.character.rect.x
		a += random.gauss(0, float(a) / 3)

		b = self.player.rect.y - self.character.rect.y
		b += random.gauss(0, float(b) / 3)

		if a > 0:
			if abs(a) > abs(b):
				self.character.posIndex = POS_RIGHT
			else:
				if b > 0:
					self.character.posIndex = POS_DOWN
				else:
					self.character.posIndex = POS_UP
		else:
			if abs(a) > abs(b):
				self.character.posIndex = POS_LEFT
			else:
				if b > 0:
					self.character.posIndex = POS_DOWN
				else:
					self.character.posIndex = POS_UP


		if a != 0 or b != 0:
			mag = math.sqrt(a*a + b*b)
			coef = float(self.enemy_speed) / mag

			self.character.speedX = a * coef
			self.character.speedY = b * coef

			self.character.rotatePosImage(time)

		self.character.move(time, collisionMap)