# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Enemy import Enemy
from RangeController import RangeController
from Weapons.WpnRifle import WpnRifle

class Nazist(Enemy):
	"""
	Contains logic for Nazist enemy.
	"""

	def __init__(self, x, y, player, director):
		Enemy.__init__(self, x, y, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player, (0, 10, 6, 10, 6, 4, 6, 8), director)
		self.controller = RangeController(self, player, director)
		self.setWeapon(WpnRifle())
		self.atk_delay_reset = 3.0 #Otherwise you don't have a chance
		self.hp = 50
