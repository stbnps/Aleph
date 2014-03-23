# -*- coding: utf-8 -*-

'''
Created on 09/03/2014

@author: DaGal
'''

from Entity import Entity
from pygame import Rect

class Weapon(Entity):
	def __init__(self, imageName=None, colorkey=None, clipRect=None, *args):
		Entity.__init__(self, 0, 0, imageName, colorkey)

		if clipRect:
			self.rect = Rect(0, 0, clipRect.w, clipRect.h)
			self.sheetCoord = [[clipRect]]

	def update(self, time, char, scene):
		pass