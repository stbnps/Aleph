# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import InitScene

class GameApp():
	def __init__(self):
		pygame.init()
		self.scene = InitScene.InitScene()
		self.clock = pygame.time.Clock()

	def run(self):
		exitGame = False

		while not exitGame:
			elapsedTime = self.clock.tick(60)

			exitGame = self.scene.update(elapsedTime)
			self.scene.draw()


if __name__ == "__main__":
	print "Hello world!"
	game = GameApp()
	game.run()
