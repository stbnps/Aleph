# -*- coding: utf-8 -*-

from Character import Character
import pygame
from EnemyController import EnemyController
from Constants import *

def blit_mask(source, dest, destpos, mask, maskrect):
	"""
	Blit an source image to the dest surface, at destpos, with a mask, using
	only the maskrect part of the mask.
	"""
	tmp = source.copy()
	tmp.blit(mask, maskrect.topleft, maskrect, special_flags=pygame.BLEND_RGBA_MULT)
	tmp.set_colorkey((0, 0, 0))
	dest.blit(tmp, destpos, dest.get_rect().clip(maskrect))


class Enemy(Character):
	"""
	Contains logic for all kinds of enemies.
	"""

	def __init__(self, x, y, imageName, colorkey, coordsName, numImages, player, magicNumbers=(0, 0, 0, 0, 0, 0, 0, 0), director=None, *args):
		Character.__init__(self, x, y, imageName, colorkey, coordsName, numImages, magicNumbers, director)
		self.controller = EnemyController(self, player, director)
		self.rect = pygame.Rect(x, y, 10, 10)
		self.atk_speed = ENEMY_ATTACK_SPEED
		self.damageCooldown = 0

	def check_died(self, scene):
		"""
		Check whether the enemy has died.
		"""
		if self.hp <= 0:
			scene.enemyGroup.remove(self)

	def hit_by_bullet(self, atk=10):
		"""
		Called when a bullet hits the enemy.
		"""
		Character.hit_by_bullet(self, atk)
		self.damageCooldown = 255


	def draw(self, screen, camera):
		Character.draw(self, screen, camera)

		if self.damageCooldown > 0:
			damageRect = pygame.Rect(0, 0, self.sheetCoord[self.posIndex][self.posImageIndex][2], self.sheetCoord[self.posIndex][self.posImageIndex][3])
			damageSurface = pygame.Surface((damageRect.w, damageRect.h))
			damageSurface.fill((255, 0, 0))

			damageSurface.set_alpha(self.damageCooldown)

			mask = pygame.transform.flip(pygame.transform.rotate(\
				self.sheet.subsurface(self.sheetCoord[self.posIndex][self.posImageIndex]), self.angle), \
				self.flipH, self.flipV).copy()
			mask = mask.convert_alpha(screen)

			blit_mask(damageSurface, screen, (self.rect.x + camera.state.x, self.rect.y + camera.state.y), mask, damageRect)
