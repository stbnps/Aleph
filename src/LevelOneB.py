# -*- coding: utf-8 -*-

from Camera import *
import pygame
from Scene import Layer, Scene
from Resources import load_image
import Constants
from Enemy import Enemy
import MessageScene
import HUD
from EntityGroup import EntityGroup
from LevelTwo import LevelTwo
from Level import Level
from Legionnaire import Legionnaire

class LevelOneB(Level):
	def __init__(self, director, player):
		Level.__init__(self, director, player)
		self.player.rect.x = 381
		self.player.rect.y = 610
		#self.enemyGroup.add([Legionnaire(987, 768, self.player),
							#Legionnaire(1083, 768, self.player),
							#Legionnaire(1119, 768, self.player)])

		self.bg = load_image("map_caesar_b_img.png", Constants.MAP_DIR)
		self.collisionBg = load_image("map_caesar_b_bg.png", Constants.BG_MAP_DIR)		
		

	def processEvent(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			nextLevel = LevelTwo(self.director, self.player)
			self.director.setScene(nextLevel)
			
		Level.processEvent(self, event)
