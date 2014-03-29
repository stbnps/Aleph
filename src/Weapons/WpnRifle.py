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

class WpnRifle(Weapon):
	def __init__(self):
		Weapon.__init__(self, "wpns-modern2.png", -1, Rect(48, 28, 24, 17), "bullet_shot.ogg", 0.5)
		self.sheetCoord[0].append(pygame.Rect(82, 25, 26, 20))
		self.cooldown = 0

	def update(self, time, char, scene):
		self.rect.clamp_ip(char.rect)

		(rx, ry, lx, ly, ux, uy, dx, dy) = char.magicNumbers
		if char.posIndex == POS_RIGHT:
			self.angle = 0
			self.rect.center = (char.rect.right + rx, char.rect.centery + ry)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_LEFT:
			self.angle = 0
			self.rect.center = (char.rect.left + lx, char.rect.centery + ly)
			self.flipH = False
			self.flipV = False
		elif char.posIndex == POS_UP:
			self.angle = -45
			self.rect.center = (char.rect.right + ux, char.rect.centery + uy)
			self.flipH = True
			self.flipV = False
		elif char.posIndex == POS_DOWN:
			self.angle = -60
			self.rect.center = (char.rect.left + dx, char.rect.centery + dy)
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
										 "bullet.png", -1, Rect(10, 10, 5, 5), damage=15)])
			self.cooldown = BOW_COOLDOWN
			self.posImageIndex = 1
			self.playSound()
