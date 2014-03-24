# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Entity import Entity
from Resources import load_sound

class Explosion(Entity):
	def __init__(self, x, y):
		Entity.__init__(self, x, y, "explosion.png", -1, "coordExplosion.txt", [25])
		self.rect.centerx = x + 2
		self.rect.bottom = y + 12

		sound = load_sound("explosion.wav")
		sound.set_volume(0.25)
		sound.play()


	def update(self, time, scene):
		# Are we in the last frame?
		lastFrame = self.posImageIndex == 24

		self.rotatePosImage(time)

		# We are in the first frame again, kill that explosion
		if lastFrame and (self.posImageIndex == 0):
			scene.bulletGroup.remove(self)
