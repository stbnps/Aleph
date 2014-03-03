# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

import pygame
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

class Layer():
	def __init__(self, director):
		self.director = director

	def update(self, *args):
		raise NotImplemented("This layer has no update method.")

	def event(self, *args):
		raise NotImplemented("This layer has no event method.")

	def draw(self, screen):
		raise NotImplemented("This layer has no draw method.")