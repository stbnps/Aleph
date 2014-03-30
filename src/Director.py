# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from Camera import *
from Scenes.MainMenu import MainMenu
import pygame

class Director():

	def __init__(self):
		pygame.mixer.pre_init(frequency=44100)
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
		pygame.display.set_caption("Aleph")
		# It's good to have player here because we can preserve it easily between levels
# 		self.scene = GameScene(self, self.player)
		self.scene = MainMenu(self)
		self.clock = pygame.time.Clock()
		self.sceneHasChanged = False

	def loop(self):
		exitGame = False
		fg = 0.0
		ft = 0.0

		while not exitGame:
			elapsedTime = self.clock.tick(60)
			fg += 1

			if elapsedTime > 16:
				ft += 1
				# print "Frames below 60 fps: " + str(100 * ft / fg) + "%"

			for event in pygame.event.get():
				exitGame = event.type == pygame.QUIT
				self.scene.processEvent(event)

			self.scene.update(elapsedTime)
			if self.sceneHasChanged:
				self.sceneHasChanged = False
				continue
			self.scene.draw(self.screen)
			pygame.display.flip()

		return exitGame

	def enqueueEvent(self, event):
		pygame.event.post(event)

	def setScene(self, scene):
		self.sceneHasChanged = True
		self.scene = scene
