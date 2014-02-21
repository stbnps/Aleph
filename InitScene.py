# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import Characters
import os

SCREEN_W = 800
SCREEN_H = 600
BORDER = 50

def load_image(name, colorkey=None):
	fullname = os.path.join('images', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', fullname
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, pygame.RLEACCEL)
	return image


class InitScene():
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
		pygame.display.set_caption("The white square adventures")
		self.player = Characters.Square(200, 200, 20, 20)
		self.bg = load_image("bg_test.png")
		self.collisioBg = self.bg.copy()
		# Yeah, this part is ok, trust me
		self.bgRect = self.bg.get_rect()
		self.screenRect = pygame.Rect(0, 0, SCREEN_W, SCREEN_H)
		self.x = 0
		self.y = 0

	# This is a bad way of doing this, but it's like in the examples.
	def scrollScreen(self, shiftX, shiftY):
		self.x += shiftX
		self.y += shiftY

		self.screenRect.left = self.x
		self.screenRect.top = self.y

	def updateScroll(self):
		if self.player.x <= BORDER:
			shift = BORDER - self.player.x
			self.player.x = BORDER

			if self.x <= 0:
				self.x = 0
			else:
				self.scrollScreen(-shift, 0)
		elif self.player.x > SCREEN_W - BORDER:
			shift = self.player.x - SCREEN_W + BORDER
			self.player.x = SCREEN_W - BORDER

			if self.x + SCREEN_W >= self.bgRect.right:
				self.x = self.bgRect.right - SCREEN_W
			else:
				self.scrollScreen(shift, 0)

		if self.player.y <= BORDER:
			shift = BORDER - self.player.y
			self.player.y = BORDER

			if self.y <= 0:
				self.y = 0
			else:
				self.scrollScreen(0, -shift)
		elif self.player.y > SCREEN_H - BORDER:
			shift = self.player.y - SCREEN_H + BORDER
			self.player.y = SCREEN_H - BORDER

			if self.y + SCREEN_H >= self.bgRect.bottom:
				self.y = self.bgRect.bottom - SCREEN_H
			else:
				self.scrollScreen(0, shift)

	def update(self, time):
		for event in pygame.event.get():

			# Si se sale del programa
			if event.type == pygame.QUIT:
				return True

		self.player.update(time, self.collisioBg, self.screenRect)
		self.updateScroll()

		return False

	def draw(self):
		self.screen.fill(0x000000)
		self.screen.blit(self.bg, self.bgRect, self.screenRect)
		self.player.draw(self.screen)
		pygame.display.flip()
