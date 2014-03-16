# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from pygame import Rect
from Item import Item
from Character import isSolid, roundToInt
import math

BULLET_SPEED = 0.3

class Bullet(Item):
	def __init__(self, x, y, speedX, speedY, imageName=None, colorkey=None, clipRect=None):
		Item.__init__(self, x, y, imageName, colorkey, clipRect)
		self.speedX = speedX
		self.speedY = speedY

		# Important if you want pinpoint accuracy
		self.floatX = float(self.rect.x)
		self.floatY = float(self.rect.y)

		self.angle = math.degrees(math.atan2(speedY, speedX))
		self.flipH = True

	def update(self, time, scene):
		self.floatX += self.speedX * time * BULLET_SPEED
		self.floatY += self.speedY * time * BULLET_SPEED
		self.rect.x = roundToInt(self.floatX)
		self.rect.y = roundToInt(self.floatY)

		if isSolid(scene.collisionBg, self.rect.x, self.rect.y):
			scene.bulletGroup.remove(self)
