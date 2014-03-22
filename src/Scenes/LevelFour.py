# -*- coding: utf-8 -*-


from Camera import *
from Level import Level
from Resources import load_image
import Constants

class LevelFour(Level):
	def __init__(self, director, player):
		Level.__init__(self, director, player)
		self.player.rect.x = 224
		self.player.rect.y = 1273

		self.bg = load_image("map_page_img.png", Constants.MAP_DIR)
		self.collisionBg = load_image("map_page_bg.png", Constants.BG_MAP_DIR)

	#def processEvent(self, event):
		#if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			#nextLevel = LevelOne(self.director, self.player)
			#self.director.setScene(nextLevel)

		#Level.processEvent(self, event)
