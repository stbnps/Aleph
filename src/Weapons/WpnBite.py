# -*- coding: utf-8 -*-

'''
Created on 20/03/2014

@author: DaGal
'''

from Weapon import Weapon
from pygame import Rect

class WpnBite(Weapon):
	def __init__(self, imageName=None, colorkey=None, clipRect=None, *args):
		Weapon.__init__(self)