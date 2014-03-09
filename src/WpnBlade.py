# -*- coding: utf-8 -*-

'''
Created on 09/03/2014

@author: DaGal
'''

from Item import *

class WpnBlade(Item):
	def __init__(self, x, y, imageName=None, colorkey=None, clipRect=None):
		Item.__init__(self, x, y, imageName, colorkey, clipRect)