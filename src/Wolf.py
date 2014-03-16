# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Enemy import Enemy

class Wolf(Enemy):
	def __init__(self, x, y, player):
		Enemy.__init__(self, x, y, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player)