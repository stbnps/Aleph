# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from pygame import Rect

SCREEN_W = 800
SCREEN_H = 600

class Camera():
	def __init__(self, width=SCREEN_W, height=SCREEN_H):
		self.state = Rect(0, 0, width, height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		l, t, _, _ = target.rect  # l = left,  t = top
		_, _, w, h = self.state  # w = width, h = height

		self.state = Rect(-l + SCREEN_W / 2, -t + SCREEN_H / 2, w, h)
