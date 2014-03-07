# -*- coding: utf-8 -*-

from Entity import Entity
import pygame
import Util
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
	def __init__(self, x, y, imageName, colorkey, coordsName, numImages, *args):
		Entity.__init__(self, x, y)
		self.speedX = 0
		self.speedY = 0
		self.controller = None

		self.sheet = Util.load_image(imageName, SPRITES_DIR, colorkey)
		coordFile = open(os.path.join(SPRITES_DIR, coordsName), "r")
		data = coordFile.read()
		coordFile.close()
		data = data.split()

		self.numImages = numImages
		self.posIndex = 0
		self.posImageIndex = 1
		self.sheetCoord = []

		n = 0

		for i in range(len(numImages)):
			tmp = []
			for j in range(numImages[i]):
				tmp.append(pygame.Rect((int(data[n])), (int(data[n + 1])), (int(data[n + 2])), (int(data[n + 3]))))
				n += 4
			self.sheetCoord.append(tmp)

		self.rect = pygame.Rect(x, y, self.sheetCoord[self.posIndex][self.posImageIndex][2], \
					 self.sheetCoord[self.posIndex][self.posImageIndex][3])

		self.timeLeftToRotate = TIME_TO_ROTATE_POS

	def rotatePosImage(self, time):
		self.timeLeftToRotate -= time

		if self.timeLeftToRotate <= 0:
			self.timeLeftToRotate = TIME_TO_ROTATE_POS
			self.posImageIndex += 1

			if self.posImageIndex >= self.numImages[self.posIndex]:
				self.posImageIndex = 0



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

	def update(self, time, collisionMap, *args):
		Entity.update(self, time, collisionMap)

	def draw(self, screen, camera):
		screen.blit(self.sheet, camera.apply(self), self.sheetCoord[self.posIndex][self.posImageIndex])
