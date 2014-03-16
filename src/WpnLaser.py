# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Weapon import Weapon
from Constants import *
import math
from Bullet import Bullet
from pygame import Rect

class WpnLaser(Weapon):
	def __init__(self):
		Weapon.__init__(self, "sw_weapons.png", -1, pygame.Rect(78, 24, 15, 18))
		self.sheetCoord[0].append(pygame.Rect(132, 21, 16, 20))
		self.cooldown = 0

	def update(self, time, char, scene):
		self.rect.clamp_ip(char.rect)

		# This magic numbers could be offsets specified for each character
		if char.posIndex == POS_RIGHT:
			self.angle = 30
			self.rect.center = (char.rect.right - 4, char.rect.centery + 6)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_LEFT:
			self.angle = 30
			self.rect.center = (char.rect.left + 4, char.rect.centery + 6)
			self.flipH = False
			self.flipV = False
		elif char.posIndex == POS_UP:
			self.angle = -45
			self.rect.center = (char.rect.right - 2, char.rect.centery + 4)
			self.flipH = False
			self.flipV = False
		elif char.posIndex == POS_DOWN:
			self.angle = -60
			self.rect.center = (char.rect.left + 2, char.rect.centery + 8)
			self.flipH = True
			self.flipV = True

		if self.cooldown > 0:
			self.cooldown -= time

			if self.cooldown < BOW_COOLDOWN * 0.75:
				self.posImageIndex = 0

		if char.attacking and (self.cooldown <= 0):
			posX = char.atkX
			posY = char.atkY

			xdist = posX - char.rect.centerx
			ydist = posY - char.rect.centery
			mag = math.sqrt(xdist * xdist + ydist * ydist)
			# mag = abs(xdist) + abs(ydist)
			scene.bulletGroup.add([Bullet(char.rect.centerx, char.rect.centery, xdist / mag , ydist / mag, \
										 "sw_weapons.png", -1, Rect(87, 349, 18, 5))])
			self.cooldown = BOW_COOLDOWN
			self.posImageIndex = 1
