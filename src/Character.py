# -*- coding: utf-8 -*-

from Entity import Entity
import pygame
from Constants import *
import os

def roundToInt(f):
	# Is there some workaround for this stupid thing?
	return int(round(f))

def isSolid(collisionMap, x, y):
	x = roundToInt(x)
	y = roundToInt(y)

	clipRect = collisionMap.get_rect()

	if (x >= clipRect.w) or (x < 0) or (y >= clipRect.h) or (y < 0):
		return True

	return collisionMap.get_at((x, y)) == (255, 0, 0, 255)

class Character(Entity):
	def __init__(self, x, y, imageName=None, colorkey=None, coordsName=None, numImages=None, *args):
		Entity.__init__(self, x, y, imageName, colorkey, coordsName, numImages)
		self.speedX = 0
		self.speedY = 0
		self.controller = None
		self.equipedWpn = None
		self.attacking = False

		if not imageName:
			self.rect = pygame.Rect(x, y, 15, 25)

	def move(self, time, collisionMap):
		shiftX = self.speedX * time
		shiftY = self.speedY * time
		rectX = self.rect.move(shiftX, 0)
		rectY = self.rect.move(0, shiftY)

		# Not the best way of doing this
		if isSolid(collisionMap, rectX.x, rectX.y) or\
			isSolid(collisionMap, rectX.x, rectX.bottom) or\
			isSolid(collisionMap, rectX.x, rectX.centery) or\
			isSolid(collisionMap, rectX.right, rectX.y) or\
			isSolid(collisionMap, rectX.right, rectX.bottom) or\
			isSolid(collisionMap, rectX.right, rectX.centery):
			shiftX = 0

		if isSolid(collisionMap, rectY.x, rectY.y) or\
			isSolid(collisionMap, rectY.x, rectY.bottom) or\
			isSolid(collisionMap, rectY.centerx, rectY.y) or\
			isSolid(collisionMap, rectY.right, rectY.y) or\
			isSolid(collisionMap, rectY.right, rectY.bottom) or\
			isSolid(collisionMap, rectY.centerx, rectY.bottom):
			shiftY = 0

		self.rect.move_ip(shiftX, shiftY)

	def setWeapon(self, weapon):
		self.equipedWpn = weapon

	def update(self, time, collisionMap):
		self.move(time, collisionMap)

		if self.equipedWpn:
			self.equipedWpn.update(time, self)

	def draw(self, screen, camera):
		Entity.draw(self, screen, camera)

		if self.equipedWpn:
			self.equipedWpn.draw(screen, camera)
