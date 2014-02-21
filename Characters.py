# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame

PLAYER_SPEED = 0.25

class Square():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speedX = 0
		self.speedY = 0
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

	# No acceleration :-)
	def move(self, time):
		self.x += self.speedX * time
		self.y += self.speedY * time
		self.rect.left = self.x
		self.rect.bottom = self.y

	def update(self, time):
		keys = pygame.key.get_pressed()
		self.speedX = 0
		self.speedY = 0

		if keys[pygame.K_DOWN]:
			self.speedY = PLAYER_SPEED
		if keys[pygame.K_UP]:
			self.speedY = -PLAYER_SPEED
		if keys[pygame.K_LEFT]:
			self.speedX = -PLAYER_SPEED
		elif keys[pygame.K_RIGHT]:
			self.speedX = PLAYER_SPEED

		self.move(time)

	def draw(self, screen):
		pygame.draw.rect(screen, 0xFFFFFF, self.rect)
