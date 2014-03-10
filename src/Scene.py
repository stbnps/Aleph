# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from Resources import clearResources

'''
Collection of objects that will be drawn at the "same" Z level
'''
class Layer():
	def __init__(self, director):
		self.director = director
		self.components = []

	def append(self, o):
		self.components.append(o)

	def update(self, time):
		for c in self.components:
			c.update(time)

	def processEvent(self, event):
		for c in self.components:
			c.processEvent(event)

	def draw(self, screen):
		for c in self.components:
			c.draw(screen)

'''
Placeholder for each game state that will be drawn, may seem similar to layer here, but when extended it won't.
'''
class Scene():
	def __init__(self, director):
		clearResources()
		self.director = director
		self.layers = []

	def append(self, layer):
		self.layers.append(layer)

	def processEvent(self, event):
		for l in self.layers:
			l.processEvent(event)

	def update(self, time):
		for l in self.layers:
			l.update(time)

	def draw(self, surface):
		for l in self.layers:
			l.draw(surface)
