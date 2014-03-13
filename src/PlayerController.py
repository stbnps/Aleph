# -*- coding: utf-8 -*-

import pygame
from Controller import Controller
from Constants import *
import math

class PlayerController(Controller):

	def __init__(self, player):
		Controller.__init__(self, player)
		self.player_speed = 0.25

	def update(self, time, collisionMap):
		keys = pygame.key.get_pressed()
		self.character.speedX = 0
		self.character.speedY = 0

		if keys[DOWN]:
			self.character.speedY = self.player_speed
			self.character.posIndex = POS_DOWN
		elif keys[UP]:
			self.character.speedY = -self.player_speed
			self.character.posIndex = POS_UP
		if keys[LEFT]:
			self.character.speedX = -self.player_speed
			self.character.posIndex = POS_LEFT
		elif keys[RIGHT]:
			self.character.speedX = self.player_speed
			self.character.posIndex = POS_RIGHT

		if self.character.speedX != 0 or self.character.speedY != 0:
			mag = math.sqrt(self.character.speedX ** 2 + self.character.speedY ** 2)
			coef = float(self.player_speed) / mag

			self.character.speedX = self.character.speedX * coef
			self.character.speedY = self.character.speedY * coef

			self.character.rotatePosImage(time)

		self.character.attacking = pygame.mouse.get_pressed()[0]

		# Look where we are trying to hit:
		if self.character.attacking:
			(posX, posY) = pygame.mouse.get_pos()
			posX += (-SCREEN_W - self.character.rect.w) / 2
			posY += (-SCREEN_H - self.character.rect.h) / 2

			if abs(posX) > abs(posY):
				if posX < 0:
					self.character.posIndex = POS_LEFT
				else:
					self.character.posIndex = POS_RIGHT
			else:
				if posY < 0:
					self.character.posIndex = POS_UP
				else:
					self.character.posIndex = POS_DOWN


		self.character.move(time, collisionMap)
		
		if self.character.equippedWpn:
			self.character.equippedWpn.update(time, self.character)
			self.character.update_attack_cooldown(time)

	def processEvent(self, event):
		# if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			# self.character.attacking = True
		pass
