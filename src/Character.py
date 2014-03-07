# -*- coding: utf-8 -*-

from Entity import Entity
import pygame

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
	def __init__(self, x, y, *args):
		Entity.__init__(self, x, y)
		self.speedX = 0
		self.speedY = 0
		self.controller = None

	def move(self, time, collisionMap):
		shiftX = self.speedX * time
		shiftY = self.speedY * time
		rect = self.rect

		# Not the best way of doing this
		if isSolid(collisionMap, rect.x + shiftX, rect.y) or\
			isSolid(collisionMap, rect.x + shiftX, rect.y + rect.h) or\
			isSolid(collisionMap, rect.x + shiftX, rect.y + rect.h / 2) or\
			isSolid(collisionMap, rect.x + shiftX + rect.w, rect.y) or\
			isSolid(collisionMap, rect.x + shiftX + rect.w, rect.y + rect.h) or\
			isSolid(collisionMap, rect.x + shiftX + rect.w, rect.y + rect.h / 2):
			shiftX = 0

		if isSolid(collisionMap, rect.x, rect.y + shiftY) or\
			isSolid(collisionMap, rect.x + rect.w, rect.y + shiftY) or\
			isSolid(collisionMap, rect.x + rect.w / 2, rect.y + shiftY) or\
			isSolid(collisionMap, rect.x, rect.y + shiftY + rect.h) or\
			isSolid(collisionMap, rect.x + rect.w, rect.y + shiftY + rect.h) or\
			isSolid(collisionMap, rect.x + rect.w / 2, rect.y + shiftY + rect.h):
			shiftY = 0

		rect.move_ip(shiftX, shiftY)

	def update(self, time, collisionMap, *args):
		Entity.update(self, time, collisionMap)
