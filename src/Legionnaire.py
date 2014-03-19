# -*- coding: utf-8 -*-


from Enemy import Enemy
from WpnBlade import WpnBlade

class Legionnaire(Enemy):
	def __init__(self, x, y, player):
		Enemy.__init__(self, x, y, "legionnaire.png", -1, "coordLegion.txt", [3, 3, 3, 3], player, (0, 10, 6, 10, 6, 4, 6, 8))
		self.setWeapon(WpnBlade())
