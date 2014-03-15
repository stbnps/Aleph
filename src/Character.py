# -*- coding: utf-8 -*-

from Entity import Entity
import pygame
from Constants import *
import os


def roundToInt(f):
	# Is there some workaround for this stupid thing?
	return int(round(f))


def isSolid(collisionMap, x, y):
	x = roundToInt(x)
	y = roundToInt(y)

	clipRect = collisionMap.get_rect()

	if (x >= clipRect.w) or (x < 0) or (y >= clipRect.h) or (y < 0):
		return True

	return collisionMap.get_at((x, y)) == (255, 0, 0, 255)


class Character(Entity):

	def __init__(self, x, y, imageName=None, colorkey=None, coordsName=None, numImages=None, *args):
		Entity.__init__(self, x, y, imageName, colorkey, coordsName, numImages)
		self.speedX = 0
		self.speedY = 0
		self.controller = None
		self.equippedWpn = None
		self.attacking = False
		self.atk_cooldown = 1.0  # Starts without cooldown

		if not imageName:
			self.rect = pygame.Rect(x, y, 15, 25)

	def move(self, time, collisionMap):
		shiftX = self.speedX * time
		shiftY = self.speedY * time
		rectX = self.rect.move(shiftX, 0)
		rectY = self.rect.move(0, shiftY)

		# Not the best way of doing this
		if self.is_colliding_x(collisionMap, rectX):
			shiftX = 0
		if self.is_colliding_y(collisionMap, rectY):
			shiftY = 0

		self.rect.move_ip(shiftX, shiftY)

	def setWeapon(self, weapon):
		self.equippedWpn = weapon

	def update(self, time, collisionMap):
		pass

	def draw(self, screen, camera):
		Entity.draw(self, screen, camera)

		if self.equippedWpn:
			self.equippedWpn.draw(screen, camera)

	def update_attack_cooldown(self, time):
		""" Reduces time remaining to next attack.
		"""
		if self.attacking:
			self.atk_cooldown -= time*PLAYER_ATTACK_SPEED
		else:
			self.atk_cooldown = 0

	def is_attacking(self):
		""" Returns true if player is atacking.
		"""
		if self.can_attack() and self.attacking:
			return True
		else:
			return False

	def can_attack(self):
		""" Returns true when the character can attack
		"""
		# De momento solo tenemos enfriamientos para no atacar chorrecientasmil veces
		# con un solo click.
		if self.atk_cooldown <= 0.0:
			self.atk_cooldown = 1.0
			return True
		else:
			return False

	def has_melee_weapon(self):
		""" Returns true if the player has equipped melee weapons.
		"""
		# De momento siempre tenemos la espadita.
		return True

	def has_distance_weapon(self):
		""" Returns true if the player has equipped distance weapons.
		"""
		# De momento si es a distancia no puede ser cuerpo a cuerpo.
		return not self.has_melee_weapon()

	def is_colliding_x(self, collisionMap, rectX):
		""" Returns true if collides in x axis.
		"""
		return  isSolid(collisionMap, rectX.x, rectX.y) or\
			isSolid(collisionMap, rectX.x, rectX.bottom) or\
			isSolid(collisionMap, rectX.x, rectX.centery) or\
			isSolid(collisionMap, rectX.right, rectX.y) or\
			isSolid(collisionMap, rectX.right, rectX.bottom) or\
			isSolid(collisionMap, rectX.right, rectX.centery)

	def is_colliding_y(self, collisionMap, rectY):
		""" Returns true if collides in y axis.
		"""
		return isSolid(collisionMap, rectY.x, rectY.y) or\
			isSolid(collisionMap, rectY.x, rectY.bottom) or\
			isSolid(collisionMap, rectY.centerx, rectY.y) or\
			isSolid(collisionMap, rectY.right, rectY.y) or\
			isSolid(collisionMap, rectY.right, rectY.bottom) or\
			isSolid(collisionMap, rectY.centerx, rectY.bottom)

	def will_collide(self, time, collisionMap):
		shiftX = self.speedX * time
		shiftY = self.speedY * time
		rectX = self.rect.move(shiftX, 0)
		rectY = self.rect.move(0, shiftY)

		# Not the best way of doing this
		if self.is_colliding_x(collisionMap, rectX) or \
		   self.is_colliding_y(collisionMap, rectY):
			return True
		else:
			return False