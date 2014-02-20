# -*- coding: utf-8 -*-

'''
Created on 20/02/2014

@author: DaGal
'''

from pygame import *

class Square():
	def __init__(self,x,y,w,h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speedX = 0
		self.speedY = 0
	
	# No acceleration :-)
	def move(self):
		self.x += self.speedX
		self.y += self.speedY
	
	def update(self):
		self.keys = key.get_pressed()
		self.speedX = 0
		self.speedY = 0
		
		if self.keys[K_DOWN]:
			self.speedY = 5
		if self.keys[K_UP]:
			self.speedY = -5
		if self.keys[K_LEFT]:
			self.speedX = -5
		elif self.keys[K_RIGHT]:
			self.speedX = 5
		
		self.move()
	
	def draw(self, screen):
		draw.rect(screen, 0xFFFFFF, Rect(self.x,self.y,self.w,self.h))