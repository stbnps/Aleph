# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

from Camera import *
from Bullet import Bullet
import pygame
from Scene import Layer, Scene
from Resources import load_image
import Constants
from Enemy import Enemy
from WpnBlade import WpnBlade
import MessageScene
import HUD
from EntityGroup import EntityGroup

BORDER = 50

class GameScene(Scene):
	def __init__(self, director, player):
		Scene.__init__(self, director)
		self.player = player
		# self.enemy = Enemy(300, 250, "player-alt.png", -1, "coordPlayerAlt2.txt", [3, 3, 3, 3], player)
		self.enemyGroup = EntityGroup([])
		# self.enemyGroup.add([Enemy(300, 280, "mr_h.png", -1, "coordMr_h.txt", [3, 3, 3, 3], player)])
		# Commenting enemies because I don't want them to colapse on into another. I'll make collisions l8r.
		# self.enemyGroup.add([Enemy(300, 280, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player)])
		# self.enemyGroup.add([Enemy(300, 280, "newton.png", -1, "coordNewton.txt", [3, 3, 3, 3], player)])
		self.enemyGroup.add([Enemy(300, 280, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player)])
		self.bg = load_image("map_newton_img.png", Constants.MAP_DIR)
		self.collisionBg = load_image("map_newton_bg.png", Constants.BG_MAP_DIR)
		# self.collisioBg = self.bg.copy()
		self.bgRect = self.bg.get_rect()
		self.camera = Camera()

		# Just one bullet at a time for now. In the future, they'll be sprites in groups...
		self.bullet = None
		# self.player.setWeapon(WpnBlade(player.rect.x, player.rect.y, "wpns2.png", -1, pygame.Rect(343, 341, 30, 30)))
		self.player.setWeapon(WpnBlade(player.rect.x, player.rect.y, "lightsaber.png", -1, pygame.Rect(128, 77, 42, 42)))

		self.HUD = HUD.HUD((0, 467), True)
		hudLayer = Layer(self.director)
		hudLayer.append(self.HUD)
		self.layers.append(hudLayer)

	def update(self, time):
		self.player.controller.update(time, self.collisionBg)
		self.enemyGroup.update(time, self.collisionBg)
		# self.enemy.controller.update(time, self.collisionBg)
		# self.player.update(time, self.collisionBg)

		if self.bullet != None:
			self.bullet.update(time)

		# self.updateScroll()
		self.camera.update(self.player)
		Scene.update(self, time)

	def processEvent(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			m = MessageScene.MessageScene(self.director, self)
			self.director.setScene(m)
		'''
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			(posX, posY) = event.pos
			posX = float(posX) - self.camera.state.left
			posY = float(posY) - self.camera.state.top
			xdist = posX - self.player.rect.left
			ydist = posY - self.player.rect.top
			mag = abs(xdist) + abs(ydist)
			self.bullet = Bullet(self.player.rect.left, self.player.rect.top, xdist / mag , ydist / mag)
		'''
		self.player.controller.processEvent(event)

	def draw(self, screen):
		screen.fill(0x000000)
		# screen.blit(self.bg, self.bgRect, self.screenRect)
		screen.blit(self.bg, self.camera.state)

		if self.bullet != None:
			self.bullet.draw(screen, self.camera)

		self.player.draw(screen, self.camera)
		# self.enemy.draw(screen, self.camera)
		self.enemyGroup.draw(screen, self.camera)
		# TODO: move maps and characters to its own layer
		Scene.draw(self, screen)  # draws rest of layers
