# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame
from Director import *

class GameApp():
	def __init__(self):
		self.director = Director()

	def run(self):
		self.director.loop()
		pygame.quit()

if __name__ == "__main__":
	game = GameApp()
	game.run()
