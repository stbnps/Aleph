# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

import pygame

PLAYER_SPEED = 0.25

def isSolid(color):
	return color != (0, 0, 0, 255)

# Is there some workaround for this stupid thing?
def roundToInt(f):
	return int(round(f))

class Square():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speedX = 0
		self.speedY = 0
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

	# No acceleration :-)
	def move(self, time, collisionMap, screenRect):
		shiftX = self.speedX * time
		shiftY = self.speedY * time

		# Not the best way of doing this
		if isSolid(collisionMap.get_at((roundToInt(self.x + shiftX + screenRect.left), roundToInt(self.y + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + shiftX + screenRect.left), roundToInt(self.y + self.h + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + shiftX + screenRect.left), roundToInt(self.y + self.h / 2 + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + shiftX + self.w + screenRect.left), roundToInt(self.y + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + shiftX + self.w + screenRect.left), roundToInt(self.y + self.h + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + shiftX + self.w + screenRect.left), roundToInt(self.y + self.h / 2 + screenRect.top)))):
			shiftX = 0

		if isSolid(collisionMap.get_at((roundToInt(self.x + screenRect.left), roundToInt(self.y + shiftY + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + self.w + screenRect.left), roundToInt(self.y + shiftY + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + self.w / 2 + screenRect.left), roundToInt(self.y + shiftY + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + screenRect.left), roundToInt(self.y + shiftY + self.h + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + self.w + screenRect.left), roundToInt(self.y + shiftY + self.h + screenRect.top)))) or\
			isSolid(collisionMap.get_at((roundToInt(self.x + self.w / 2 + screenRect.left), roundToInt(self.y + shiftY + self.h + screenRect.top)))):
			shiftY = 0

		self.x += shiftX
		self.y += shiftY
		self.rect.left = self.x
		self.rect.top = self.y

	def update(self, time, collisionMap, screenRect):
		keys = pygame.key.get_pressed()
		self.speedX = 0
		self.speedY = 0

		if keys[pygame.K_s]:
			self.speedY = PLAYER_SPEED
		elif keys[pygame.K_w]:
			self.speedY = -PLAYER_SPEED
		if keys[pygame.K_a]:
			self.speedX = -PLAYER_SPEED
		elif keys[pygame.K_d]:
			self.speedX = PLAYER_SPEED

		self.move(time, collisionMap, screenRect)

	def draw(self, screen):
		pygame.draw.rect(screen, 0xFFFFFF, self.rect)


# Yea, bullet is a character for now :-)
class Bullet():
	def __init__(self, x, y, speedX, speedY):
		self.x = x
		self.y = y
		self.speedX = speedX
		self.speedY = speedY
		self.rect = pygame.Rect(self.x, self.y, 2, 2)

		print "Bullet created at %f %f with speed %f %f" % (x, y, speedX, speedY)


	def move(self, time):
		self.x += self.speedX * time
		self.y += self.speedY * time
		self.rect.left = self.x
		self.rect.top = self.y

	def update(self, time):
		self.move(time)

	def draw(self, screen):
		pygame.draw.rect(screen, 0xFFFFFF, self.rect)
