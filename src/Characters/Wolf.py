# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Weapons.WpnBite import WpnBite
from Enemy import Enemy

class Wolf(Enemy):
	"""
	Contains logic for Wolf enemies.
	"""

	def __init__(self, x, y, player, director):
		Enemy.__init__(self, x, y, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player, director=director)
		self.equippedWpn = WpnBite()