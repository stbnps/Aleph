# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

from Layer import *
from Camera import *
from Bullet import Bullet

BORDER = 50

class InitScene(Layer):
	def __init__(self, director, player):
		Layer.__init__(self, director)
		self.player = player
		self.bg = load_image("map_newton.png")
		self.collisionBg = load_image("map_newton_bg.png")
		# self.collisioBg = self.bg.copy()
		self.bgRect = self.bg.get_rect()
		self.camera = Camera()

		# Just one bullet at a time for now. In the future, they'll be sprites in groups...
		self.bullet = None

	def scrollScreen(self, shiftX, shiftY):
		# This is a bad way of doing this, but it's like in the examples.
		self.x += shiftX
		self.y += shiftY

		self.screenRect.left = self.x
		self.screenRect.top = self.y

	def updateScroll(self):
		if self.player.x <= BORDER:
			shift = BORDER - self.player.x
			self.player.x = BORDER

			if self.x <= 0:
				self.x = 0
			else:
				self.scrollScreen(-shift, 0)
		elif self.player.x > SCREEN_W - BORDER:
			shift = self.player.x - SCREEN_W + BORDER
			self.player.x = SCREEN_W - BORDER

			if self.x + SCREEN_W >= self.bgRect.right:
				self.x = self.bgRect.right - SCREEN_W
			else:
				self.scrollScreen(shift, 0)

		if self.player.y <= BORDER:
			shift = BORDER - self.player.y
			self.player.y = BORDER

			if self.y <= 0:
				self.y = 0
			else:
				self.scrollScreen(0, -shift)
		elif self.player.y > SCREEN_H - BORDER:
			shift = self.player.y - SCREEN_H + BORDER
			self.player.y = SCREEN_H - BORDER

			if self.y + SCREEN_H >= self.bgRect.bottom:
				self.y = self.bgRect.bottom - SCREEN_H
			else:
				self.scrollScreen(0, shift)

	def update(self, time):
		self.player.update(time, self.collisionBg)

		if self.bullet != None:
			self.bullet.update(time)

		# self.updateScroll()
		self.camera.update(self.player)

	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				(posX, posY) = event.pos
				posX = float(posX) - self.camera.state.left
				posY = float(posY) - self.camera.state.top
				xdist = posX - self.player.rect.left
				ydist = posY - self.player.rect.top
				mag = abs(xdist) + abs(ydist)
				self.bullet = Bullet(self.player.rect.left, self.player.rect.top, xdist / mag , ydist / mag)

	def draw(self, screen):
		screen.fill(0x000000)
		# screen.blit(self.bg, self.bgRect, self.screenRect)
		screen.blit(self.bg, self.camera.state)

		if self.bullet != None:
			self.bullet.draw(screen, self.camera)

		self.player.draw(screen, self.camera)
