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
	def __init__(self, creator, x, y, speedX, speedY, imageName=None, colorkey=None, clipRect=None, damage=10):
		Weapon.__init__(self, imageName, colorkey, clipRect)
		self.rect = Rect(x, y, 10, 10)
		self.speedX = speedX
		self.speedY = speedY
		self.atk = damage
		self.creator = creator

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
		if sprite.collide_rect(self, scene.player) and not self.creator.__class__.__name__ == scene.player.__class__.__name__:
				scene.player.receive_attack(self.atk)
				scene.bulletGroup.remove(self)
		hitted_players = sprite.spritecollide(self, scene.enemyGroup, False)
		# scene.bulletGroup.remove(self)
		for player in hitted_players:
			# Friendly fire
			if self.creator.__class__.__name__ == player.__class__.__name__:
				continue
			player.receive_attack(self.atk)
			# A bullet should not be capable of going through an infinite amount of bodies
			scene.bulletGroup.remove(self)
			break

