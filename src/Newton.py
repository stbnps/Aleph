# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Enemy import Enemy
from WpnGrenade import WpnGrenade

class Newton(Enemy):
	def __init__(self, x, y, player):
		Enemy.__init__(self, x, y, "newton.png", -1, "coordNewton.txt", [3, 3, 3, 3], player)
		self.setWeapon(WpnGrenade())