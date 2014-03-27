# -*- coding: utf-8 -*-

from Constants import *

class Controller():
	"""
	Abstract class that contains the logic to control a Character behavior.
	"""

	def __init__(self, character, director = None):
		self.character = character
		self.director = director

	def update(self, time, scene):
		"""
		Updates the state.
		"""
		pass

	def processEvent(self, event):
		"""
		Processes a pygame event.
		"""
		pass

	def update_pos(self, speed_x, speed_y):
		"""
		Sets position of the sprite given Character's speed.
		"""
		if speed_x > 0:
			if abs(speed_x) > abs(speed_y):
				self.character.posIndex = POS_RIGHT
			else:
				if speed_y > 0:
					self.character.posIndex = POS_DOWN
				else:
					self.character.posIndex = POS_UP
		else:
			if abs(speed_x) > abs(speed_y):
				self.character.posIndex = POS_LEFT
			else:
				if speed_y > 0:
					self.character.posIndex = POS_DOWN
				else:
					self.character.posIndex = POS_UP
