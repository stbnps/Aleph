# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Enemy import Enemy
from Weapons.WpnGrenade import WpnGrenade
from pygame import event, USEREVENT
from Events import *

class Newton(Enemy):
	"""
	Contains logic for Newton enemy.
	"""

	def __init__(self, x, y, player, director):
		Enemy.__init__(self, x, y, "newton.png", -1, "coordNewton.txt", [3, 3, 3, 3], player, director=director)
		self.setWeapon(WpnGrenade())


	def check_died(self, scene):
		"""
		Check whether this enemy has died.
		"""
		if self.hp <= 0:
			scene.enemyGroup.remove(self)
			event.post(event.Event(USEREVENT, code=NEWTONDEAD))
