# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

from Camera import *
from Bullet import Bullet
import pygame
from Scene import Layer, Scene
from Util import load_image
import Constants

BORDER = 50

class GameScene(Scene):
	def __init__(self, director, player, enemy):
		Scene.__init__(self, director)
		self.player = player
		self.enemy = enemy
		self.bg = load_image("map_newton_img.png", Constants.MAP_DIR)
		self.collisionBg = load_image("map_newton_bg.png", Constants.BG_MAP_DIR)
		# self.collisioBg = self.bg.copy()
		self.bgRect = self.bg.get_rect()
		self.camera = Camera()

		# Just one bullet at a time for now. In the future, they'll be sprites in groups...
		self.bullet = None

	def update(self, time):
		self.player.controller.update(time, self.collisionBg)
		self.enemy.controller.update(time, self.collisionBg)
		# self.player.update(time, self.collisionBg)

		if self.bullet != None:
			self.bullet.update(time)

		# self.updateScroll()
		self.camera.update(self.player)

	def processEvent(self, event):
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
		self.enemy.draw(screen, self.camera)
