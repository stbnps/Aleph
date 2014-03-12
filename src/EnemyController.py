# -*- coding: utf-8 -*-

from Controller import Controller
from Constants import *
import math
import random

class EnemyController(Controller):

	def __init__(self, enemy, player):
		Controller.__init__(self, enemy)
		self.player = player
		self.enemy_speed = 0.10

	def update(self, time, collisionMap):
		self.character.speedX = 0
		self.character.speedY = 0
		self.follow_player(time)
		if self.check_melee_hit():		
			print "%s man dao una ostia!" % self
		Controller.update(self, time, collisionMap)

	

	def check_melee_hit(self):
		""" Returns true when been atacked with a melee weapon.
		"""
		return self.player.is_atacking() and self.colides_with_player() and self.player.has_melee_weapon()


	def colides_with_player(self):
		""" Returns true if the enemy overlaps the player.
			Note: It has a small 30 u. margin
		"""
		overlaps_y = abs(self.player.rect.y - self.character.rect.y) < 30 
		overlaps_x = abs(self.player.rect.x - self.character.rect.x) < 30
		return  overlaps_x and overlaps_y
	
	

	def detect_player(self, detection_range=80):
		""" The enemy only detects player in range.
		"""

		delta_x = self.player.rect.x - self.character.rect.x
		delta_y = self.player.rect.y - self.character.rect.y		
		delta_x += random.gauss(0, float(delta_x) / 3)
		delta_y += random.gauss(0, float(delta_y) / 3)

		distance = math.sqrt(delta_x * delta_x + delta_y * delta_y)

		return distance < detection_range


	def follow_player(self, time):
		""" Makes the enemy follow the player if the player is near.
		"""
		if not self.detect_player():
			return
		
		# Calculatelayer relative position
		delta_x = self.player.rect.x - self.character.rect.x
		delta_x += random.gauss(0, float(delta_x) / 3)

		delta_y = self.player.rect.y - self.character.rect.y
		delta_y += random.gauss(0, float(delta_y) / 3)

		#Update sprite
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

		# Move enemy			
		if abs(delta_x) > 30 or abs(delta_y) > 30:
			mag = math.sqrt(delta_x * delta_x + delta_y * delta_y)
			coef = float(self.enemy_speed) / mag

			self.character.speedX = delta_x * coef
			self.character.speedY = delta_y * coef

			self.character.rotatePosImage(time)