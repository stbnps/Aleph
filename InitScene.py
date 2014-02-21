# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import Characters

class InitScene():
	def __init__(self):
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("The white square adventures")
		self.player = Characters.Square(200, 200, 20, 20)

	def update(self, time):
		for event in pygame.event.get():

			# Si se sale del programa
			if event.type == pygame.QUIT:
				return True

		self.player.update(time)

		return False

	def draw(self):
		self.screen.fill(0x000000)
		self.player.draw(self.screen)
		pygame.display.flip()
