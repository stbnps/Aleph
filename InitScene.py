# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import Characters
import os

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
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("The white square adventures")
		self.player = Characters.Square(200, 200, 20, 20)
		self.bg = load_image("field_bg.jpg")

	def update(self, time):
		for event in pygame.event.get():

			# Si se sale del programa
			if event.type == pygame.QUIT:
				return True

		self.player.update(time)

		return False

	def draw(self):
		self.screen.fill(0x000000)
		self.screen.blit(self.bg, self.screen.get_rect())
		self.player.draw(self.screen)
		pygame.display.flip()
