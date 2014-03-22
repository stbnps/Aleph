# -*- coding: utf-8 -*-

'''
Created on 09/03/2014

@author: DaGal
'''

from Weapon import Weapon
from Constants import *
import math

class WpnBlade(Weapon):
	def __init__(self, imageName=None, colorkey=None, clipRect=None):
		Weapon.__init__(self, imageName, colorkey, clipRect)
		self.attackAngle = 0
		self.hip = math.sqrt(self.rect.w * self.rect.w + self.rect.h * self.rect.h)

	def update(self, time, char, scene):
		self.rect.clamp_ip(char.rect)

		# This magic numbers could be offsets specified for each character
		if char.posIndex == POS_RIGHT:
			self.angle = 0
			self.rect.center = (char.rect.right - 4, char.rect.centery + 8)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_LEFT:
			self.angle = 0
			self.rect.center = (char.rect.left + 4, char.rect.centery + 6)
			self.flipH = False
			self.flipV = False
		elif char.posIndex == POS_UP:
			self.angle = -25
			self.rect.center = (char.rect.right - 2, char.rect.centery + 8)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_DOWN:
			self.angle = -25
			self.rect.center = (char.rect.left, char.rect.centery + 8)
			self.flipH = True
			self.flipV = True

		if char.attacking:
			# Let the mighty sword swing!
			if self.attackAngle > BLADE_SWING_ANGLE:
				self.attackAngle = 0

			self.attackAngle += PLAYER_ATTACK_SPEED * BLADE_SWING_ANGLE * time
			self.angle += self.attackAngle - (BLADE_SWING_ANGLE / 2)


		else:
			self.attackAngle = 0

		# Compensate a weird rotation effect
		offset = min(abs(math.sin(math.radians(self.angle))), abs(math.cos(math.radians(self.angle)))) / math.sqrt(2)
		self.rect.move_ip((self.rect.w - self.hip) * offset, (self.rect.h - self.hip) * offset)
