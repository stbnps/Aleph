# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import Characters

class InitScene():
	def __init__(self):
		self.screen = pygame.display.set_mode((600,400))
		self.square = Characters.Square(200,200,50,50)
	
	def update(self):
		for event in pygame.event.get():

			# Si se sale del programa
			if event.type == pygame.QUIT:
				return True
			
		self.square.update()
		#self.square.draw(self.screen)
		
		return False
	
	def draw(self):
		self.screen.fill(0x000000)
		#pygame.draw.rect(self.screen, 0xFFFFFF, pygame.Rect(0,0,600,400))
		self.square.draw(self.screen)
		pygame.display.flip()