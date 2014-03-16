# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from Entity import Entity
from pygame import Rect

BULLET_SPEED = 0.5

class Bullet(Entity):
	def __init__(self, x, y, speedX, speedY, *args):
		Entity.__init__(self, x, y)
		self.speedX = speedX
		self.speedY = speedY
		self.rect = Rect(x, y, 2, 2)

		print "Bullet created at %f %f with speed %f %f" % (x, y, speedX, speedY)

	def update(self, time, scene):
		self.rect.move_ip(self.speedX * time * BULLET_SPEED, self.speedY * time * BULLET_SPEED)
