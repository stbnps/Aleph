# -*- coding: utf-8 -*-

from Entity import Entity
import pygame
from Constants import *
import os

class Door(Entity):
	def __init__(self, x, y, imageName=None, colorkey=None, coordsName=None, numImages=None, *args):
		Entity.__init__(self, x, y, imageName, colorkey, coordsName, numImages)
		self.active = False
		self.posIndex = POS_UP
		self.posImageIndex = 0
		
	def setActive(self, active):
		self.active = active
		
	def update(self, time, scene):
		if self.active:
			self.posImageIndex = 1	
		
		
		
