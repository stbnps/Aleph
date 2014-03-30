# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Weapon import Weapon
from Constants import *
import math
from pygame import Rect
from ThrowedGrenade import ThrowedGrenade

class WpnGrenade(Weapon):
	def __init__(self):
		Weapon.__init__(self, "items-1small.png", None, Rect(110, 120, 9, 11))
		self.cooldown = 0

	def update(self, time, char, scene):
		self.rect.clamp_ip(char.rect)

		# This magic numbers could be offsets specified for each character
		if char.posIndex == POS_RIGHT:
			self.rect.center = (char.rect.right - 4, char.rect.centery + 8)
		elif char.posIndex == POS_LEFT:
			self.rect.center = (char.rect.left + 4, char.rect.centery + 6)
		elif char.posIndex == POS_UP:
			self.rect.center = (char.rect.right - 2, char.rect.centery + 8)
		elif char.posIndex == POS_DOWN:
			self.rect.center = (char.rect.left, char.rect.centery + 8)

		if self.cooldown > 0:
			self.cooldown -= time

		if char.attacking and (self.cooldown <= 0):
			posX = char.atkX
			posY = char.atkY

			xdist = posX - char.rect.centerx
			ydist = posY - char.rect.centery
			mag = math.sqrt(xdist * xdist + ydist * ydist)
			# mag = abs(xdist) + abs(ydist)
			scene.bulletGroup.add([ThrowedGrenade(char, char.rect.centerx, char.rect.centery, xdist / mag , ydist / mag, mag)])
			self.cooldown = BOW_COOLDOWN
