# -*- coding: utf-8 -*-

from pygame.sprite import *
from Resources import load_image
from Constants import *
import os

class Entity(Sprite):
	def __init__(self, x, y, imageName=None, colorkey=None, coordsName=None, numImages=None, *args):
		Sprite.__init__(self)

		if imageName:
			self.sheet = load_image(imageName, SPRITES_DIR, colorkey)

			if coordsName:
				coordFile = open(os.path.join(SPRITES_DIR, coordsName), "r")
				data = coordFile.read()
				coordFile.close()
				data = data.split()

				if numImages:
					self.numImages = numImages
				else:
					self.numImages = [1]
				self.posIndex = 0
				self.posImageIndex = 0
				self.sheetCoord = []

				n = 0

				for i in range(len(numImages)):
					tmp = []
					for _ in range(numImages[i]):
						tmp.append(pygame.Rect((int(data[n])), (int(data[n + 1])), (int(data[n + 2])), (int(data[n + 3]))))
						n += 4
					self.sheetCoord.append(tmp)

				self.rect = pygame.Rect(x, y, self.sheetCoord[self.posIndex][self.posImageIndex][2], \
							 self.sheetCoord[self.posIndex][self.posImageIndex][3])

				self.timeLeftToRotate = TIME_TO_ROTATE_POS
			else:
				self.numImages = [1]
				self.posIndex = 0
				self.posImageIndex = 0
				self.rect = self.sheet.get_rect()
				self.sheetCoord = [[self.rect]]
				self.timeLeftToRotate = None
		else:
			self.sheet = None
			self.timeLeftToRotate = None
			self.rect = pygame.Rect(x, y, 0, 0)

		self.flipH = False
		self.flipV = False
		self.angle = 0

	def rotatePosImage(self, time):
		if self.timeLeftToRotate:
			self.timeLeftToRotate -= time

			if self.timeLeftToRotate <= 0:
				self.timeLeftToRotate = TIME_TO_ROTATE_POS
				self.posImageIndex += 1

				if self.posImageIndex >= self.numImages[self.posIndex]:
					self.posImageIndex = 0

	def update(self, time, scene):
		pass

	def draw(self, screen, camera):
		if self.sheet:
			# screen.blit(pygame.transform.flip(self.sheet.subsurface(self.sheetCoord[self.posIndex][self.posImageIndex]), self.flipH, False), camera.apply(self))
			screen.blit(pygame.transform.flip(pygame.transform.rotate(\
				self.sheet.subsurface(self.sheetCoord[self.posIndex][self.posImageIndex]), self.angle), \
				self.flipH, self.flipV), camera.apply(self))
		else:
			pygame.draw.rect(screen, 0xFFFFFF, camera.apply(self))
