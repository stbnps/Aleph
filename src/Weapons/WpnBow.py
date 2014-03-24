# -*- coding: utf-8 -*-

'''
Created on 15/03/2014

@author: DaGal
'''

from Weapon import Weapon
from Constants import *
import math
from Bullet import Bullet
from pygame import Rect

class WpnBow(Weapon):
	def __init__(self, imageName=None, colorkey=None, clipRect=None):
		Weapon.__init__(self, imageName, colorkey, clipRect, "bow_shot.wav")
		self.cooldown = 0

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

		if self.cooldown > 0:
			self.cooldown -= time

		if char.attacking and (self.cooldown <= 0):
			posX = char.atkX
			posY = char.atkY

			xdist = posX - char.rect.centerx
			ydist = posY - char.rect.centery
			mag = math.sqrt(xdist * xdist + ydist * ydist)
			# mag = abs(xdist) + abs(ydist)
			scene.bulletGroup.add([Bullet(char.rect.centerx, char.rect.centery, xdist / mag , ydist / mag, \
										 "arrow.png", -1, Rect(88, 28, 16, 7))])
			self.cooldown = BOW_COOLDOWN
			self.playSound()
