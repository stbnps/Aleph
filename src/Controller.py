# -*- coding: utf-8 -*-

class Controller():

	def __init__(self, character):
		self.character = character

	def update(self, time, collisionMap):
		self.character.update(time, collisionMap)

	def processEvent(self, event):
		pass
