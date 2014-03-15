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
from Level import Level

class LevelThree(Level):
	def __init__(self, director, player):
		Level.__init__(self, director, player)
		self.player.rect.x = 766
		self.player.rect.y = 82

		self.enemyGroup.add([Enemy(640, 140, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(640, 176, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(688, 18, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(524, 51, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(524, 140, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(345, 46, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(345, 70, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(345, 100, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(140, 145, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(140, 175, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(185, 10, "nazist.png", -1, "coordNazist.txt", [3, 3, 3, 3], player),
							Enemy(27, 48, "mr_h.png", -1, "coordMr_h.txt", [3, 3, 3, 3], player)])


		self.bg = load_image("mapa_h.png", Constants.MAP_DIR)
		self.collisionBg = load_image("mapa_h_bg.png", Constants.BG_MAP_DIR)
