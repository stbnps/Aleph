# -*- coding: utf-8 -*-

'''
Created on 09/03/2014

@author: DaGal
'''

from Item import *
from Constants import *

class WpnBlade(Item):
	def __init__(self, x, y, imageName=None, colorkey=None, clipRect=None):
		Item.__init__(self, x, y, imageName, colorkey, clipRect)
		self.attackAngle = 0

	def update(self, time, char):
		self.rect.clamp_ip(char.rect)
		self.rect.move_ip(0, 2)

		# It would be nice to also rotate it a little bit.
		if char.posIndex == POS_RIGHT:
			self.angle = 0
			self.rect.move_ip(10, 0)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_LEFT:
			self.angle = 0
			self.rect.move_ip(-8, 0)
			self.flipH = False
			self.flipV = False
		elif char.posIndex == POS_UP:
			self.angle = -25
			self.rect.move_ip(8, -4)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_DOWN:
			self.angle = -25
			self.rect.move_ip(-4, 12)
			self.flipH = True
			self.flipV = True

		if char.attacking:
			# Let the mighty sword swing!
			if self.attackAngle > BLADE_SWING_ANGLE:
				self.attackAngle = 0

			self.attackAngle += BLADE_SWING_SPEED * time
			self.angle += self.attackAngle - BLADE_SWING_ANGLE / 2

			# Compensate a weird rotation effect
			if char.posIndex == POS_RIGHT or char.posIndex == POS_LEFT:
				self.rect.move_ip(-4 + 0.02 * self.attackAngle, -0.05 * (BLADE_SWING_ANGLE - self.attackAngle))
			else:
				self.rect.move_ip(-4 + 0.08 * self.attackAngle, -4 + 0.06 * (BLADE_SWING_ANGLE - self.attackAngle))
		else:
			self.attackAngle = 0
