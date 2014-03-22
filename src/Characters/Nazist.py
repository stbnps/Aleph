# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Enemy import Enemy
from Weapons.WpnRifle import WpnRifle

class Nazist(Enemy):
	def __init__(self, x, y, player):
		Enemy.__init__(self, x, y, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player, (0, 10, 6, 10, 6, 4, 6, 8))
		self.setWeapon(WpnRifle())