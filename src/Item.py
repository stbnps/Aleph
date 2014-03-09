# -*- coding: utf-8 -*-

'''
Created on 09/03/2014

@author: DaGal
'''

from Entity import *

class Item(Entity):
	def __init__(self, x, y, imageName=None, colorkey=None, clipRect=None, *args):
		Entity.__init__(self, x, y, imageName, colorkey)

		if clipRect:
			self.rect = pygame.Rect(x, y, clipRect.w, clipRect.h)
			self.sheetCoord = [[clipRect]]
