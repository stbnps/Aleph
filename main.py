# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
import InitScene
from Director import *

class GameApp():
	def __init__(self):
		pygame.init()
		self.director = Director()

	def run(self):
		self.director.loop()
		pygame.quit()


if __name__ == "__main__":
	print "Hello world!"
	game = GameApp()
	game.run()
