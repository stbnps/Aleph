# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import sys
import InitScene

class GameApp():
	def __init__(self):
		pygame.init()
		self.scene = InitScene.InitScene()
		self.clock = pygame.time.Clock()
		
	def run(self):
		while True:
			#not sure this is the right way to do this, but it's like they want
			elapsedTime = self.clock.tick(60)
			
			exit = self.scene.update()
			self.scene.draw()
			
			if exit:
				sys.exit(0)
		

if __name__ == "__main__":
	print "Hello world!"
	game = GameApp()
	game.run()