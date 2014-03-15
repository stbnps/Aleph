# -*- coding: utf-8 -*-

'''
Created on 15/02/2014

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
from LevelThree import LevelThree
from Level import Level

class LevelTwo(Level):
	def __init__(self, director, player):
		Level.__init__(self, director, player)
		self.player.rect.x = 200
		self.player.rect.y = 200
		self.enemyGroup.add([Enemy(300, 280, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(281, 72, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(422, 57, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(737, 160, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(737, 190, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(300, 280, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(500, 380, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(315, 495, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(217, 662, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(572, 666, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(917, 413, "wolves.png", -1, "coordWolves.txt", [3, 3, 3, 3], player),
							Enemy(896, 851, "newton.png", -1, "coordNewton.txt", [3, 3, 3, 3], player)])

		self.bg = load_image("map_newton_img.png", Constants.MAP_DIR)
		self.collisionBg = load_image("map_newton_bg.png", Constants.BG_MAP_DIR)

	def processEvent(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			nextLevel = LevelThree(self.director, self.player)
			self.director.setScene(nextLevel)

		Level.processEvent(self, event)