# -*- coding: utf-8 -*-

from Constants import *

class Controller():

	def __init__(self, character, director = None):
		self.character = character
		self.director = director

	def update(self, time, scene):
		pass

	def processEvent(self, event):
		pass

	def update_pos(self, delta_x, delta_y):
		if delta_x > 0:
			if abs(delta_x) > abs(delta_y):
				self.character.posIndex = POS_RIGHT
			else:
				if delta_y > 0:
					self.character.posIndex = POS_DOWN
				else:
					self.character.posIndex = POS_UP
		else:
			if abs(delta_x) > abs(delta_y):
				self.character.posIndex = POS_LEFT
			else:
				if delta_y > 0:
					self.character.posIndex = POS_DOWN
				else:
					self.character.posIndex = POS_UP
