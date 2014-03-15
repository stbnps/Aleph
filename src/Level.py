# -*- coding: utf-8 -*-

'''
Created on 15/03/2014

@author: DaGal
'''

from Scene import Scene, Layer
from EntityGroup import EntityGroup
from Camera import Camera
from HUD import HUD
import pygame
from MessageScene import MessageScene

class Level(Scene):
	def __init__(self, director, player):
		Scene.__init__(self, director)
		self.player = player
		self.enemyGroup = EntityGroup([])

		self.bg = None
		self.collisionBg = None
		self.camera = Camera()

		self.HUD = HUD((0, 467), True)
		hudLayer = Layer(self.director)
		hudLayer.append(self.HUD)
		self.layers.append(hudLayer)

	def update(self, time):
		Scene.update(self, time)

		if self.collisionBg != None:
			self.player.update(time, self.collisionBg)
			self.enemyGroup.update(time, self.collisionBg)

		self.camera.update(self.player)

	def processEvent(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			m = MessageScene(self.director, self)
			self.director.setScene(m)

		self.player.controller.processEvent(event)

	def draw(self, screen):
		screen.fill(0x000000)

		if self.bg:
			screen.blit(self.bg, self.camera.state)

		self.enemyGroup.draw(screen, self.camera)
		self.player.draw(screen, self.camera)
		# TODO: move maps and characters to its own layer
		Scene.draw(self, screen)  # draws rest of layers
