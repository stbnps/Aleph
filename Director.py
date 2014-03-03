# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

import pygame
import sys
from InitScene import *
from Camera import *
from Player import Player

class Director():

	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
		pygame.display.set_caption("The white square adventures")
		self.player = Player(200, 200)
		# It's good to have player here because we can preserve it easily between levels
		self.scene = InitScene(self, self.player)
		self.clock = pygame.time.Clock()

	def loop(self):
		exitGame = False

		while not exitGame:
			elapsedTime = self.clock.tick(60)

			for event in pygame.event.get():
				exitGame = event.type == pygame.QUIT
				self.scene.event(event)

			self.scene.update(elapsedTime)
			self.scene.draw(self.screen)
			pygame.display.flip()

		return exitGame

	def enqueueEvent(self, event):
		pygame.event.post(event)
