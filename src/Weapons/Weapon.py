# -*- coding: utf-8 -*-

'''
Created on 09/03/2014

@author: DaGal
'''

from Entity import Entity
from pygame import Rect
from Resources import load_sound

class Weapon(Entity):
	def __init__(self, imageName=None, colorkey=None, clipRect=None, sound=None, soundVolume=1, *args):
		Entity.__init__(self, 0, 0, imageName, colorkey)

		if clipRect:
			self.rect = Rect(0, 0, clipRect.w, clipRect.h)
			self.sheetCoord = [[clipRect]]

		if sound:
			self.sound = load_sound(sound)
			self.sound.set_volume(soundVolume)
		else:
			self.sound = None

		self.melee = False

	def playSound(self):
		if self.sound:
			self.sound.play()

	def stopSound(self):
		if self.sound:
			self.sound.stop()

	def update(self, time, char, scene):
		pass
