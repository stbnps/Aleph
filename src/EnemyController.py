# -*- coding: utf-8 -*-

from Controller import Controller
from Constants import *
import math
import random
import pygame

DETECTION_RANGE = 200
MAX_TIMES_COLLIDED = 10

class EnemyController(Controller):

	current_direction = POS_UP
	previous_x = 0

	def __init__(self, enemy, player):
		Controller.__init__(self, enemy)
		self.player = player
		self.enemy_speed = 0.10
		self.ttl = 0
		self.lastSpeedX = 0
		self.lastSpeedY = 0


	def update(self, time, scene):
		collisionMap = scene.collisionBg
		self.character.speedX = 0
		self.character.speedY = 0
		self.move_behavior(time, collisionMap, scene)

		if self.check_melee_hit():
			print "%s man dao una ostia!" % self

		if self.character.equippedWpn:
			self.character.equippedWpn.update(time, self.character, scene)
			self.character.update_attack_cooldown(time)


	def check_melee_hit(self):
		""" Returns true when been attacked with a melee weapon.
		"""
		return self.player.is_attacking() and self.collides_with_player() and self.player.has_melee_weapon()


	def collides_with_player(self):
		""" Returns true if the enemy overlaps the player.
			Note: It has a small 30 u. margin
		"""
		overlaps_y = abs(self.player.rect.y - self.character.rect.y) < 30
		overlaps_x = abs(self.player.rect.x - self.character.rect.x) < 30
		return  overlaps_x and overlaps_y


	def detect_player(self, detection_range=DETECTION_RANGE):
		""" The enemy only detects player in range.
		"""

		delta_x = self.player.rect.x - self.character.rect.x
		delta_y = self.player.rect.y - self.character.rect.y

		distance = math.sqrt(delta_x * delta_x + delta_y * delta_y)

		return distance < detection_range


	def follow_player(self, time, collisionMap):
		""" Makes the enemy follow the player if the player is near.
		"""

		# Calculatelayer relative position
		delta_x = self.player.rect.x - self.character.rect.x
		delta_y = self.player.rect.y - self.character.rect.y
		distance = math.sqrt(delta_x * delta_x + delta_y * delta_y)

		if (distance > DETECTION_RANGE):
			return False

		# Move enemy
		if distance > 20:
			coef = float(self.enemy_speed) / distance

			self.character.speedX = delta_x * coef
			self.character.speedY = delta_y * coef

		return True


	def random_move(self, time, collisionMap):
		def new_random_move():
			self.ttl = random.randint(10, 100)
			self.lastSpeedX = random.gauss(0, 0.1)
			self.lastSpeedY = random.gauss(0, 0.1)
			distance = math.sqrt(self.lastSpeedX ** 2 + self.lastSpeedY ** 2)
			coef = float(self.enemy_speed) / distance
			self.lastSpeedX = self.lastSpeedX * coef
			self.lastSpeedY = self.lastSpeedY * coef

		if self.ttl == 0:
			new_random_move()
		else:
			self.ttl -= 1

		self.character.speedX = self.lastSpeedX
		self.character.speedY = self.lastSpeedY

		timesCollided = 0

		while (timesCollided < MAX_TIMES_COLLIDED) and \
		      (self.character.will_collide(time, collisionMap)):
			timesCollided += 1
			new_random_move()
			self.character.speedX = self.lastSpeedX
			self.character.speedY = self.lastSpeedY

		return True

	def avoid_enemy_overlap(self, scene):
		if len(pygame.sprite.spritecollide(self.character, scene.enemyGroup, False)) > 1:
			if bool(random.getrandbits(1)):
				self.character.speedX = -self.character.speedX
				self.character.speedY = -self.character.speedY

	def move_behavior(self, time, collisionMap, scene):
		if not self.follow_player(time, collisionMap):
			self.random_move(time, collisionMap)	

		self.avoid_enemy_overlap(scene)	

		self.update_pos(self.character.speedX, self.character.speedY)
		self.character.rotatePosImage(time)
		self.character.move(time, scene)
