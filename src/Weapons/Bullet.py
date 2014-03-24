# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from pygame import Rect, sprite
from Weapon import Weapon
from Characters.Character import isSolid, roundToInt
import math

BULLET_SPEED = 0.3

class Bullet(Weapon):
	def __init__(self, x, y, speedX, speedY, imageName=None, colorkey=None, clipRect=None):
		Weapon.__init__(self, imageName, colorkey, clipRect)
		self.rect = Rect(x, y, 0, 0)
		self.speedX = speedX
		self.speedY = speedY
		self.atk = 5

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

		self.kill_people(scene)


	def kill_people(self, scene):
		hitted_players = sprite.spritecollide(self, scene.enemyGroup, False)
		# scene.bulletGroup.remove(self)
		for player in hitted_players:
			player.hit_by_bullet(self.atk)
			# A bullet should not be capable of going through an infinite amount of bodies
			scene.bulletGroup.remove(self)

