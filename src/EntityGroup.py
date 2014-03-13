# -*- coding: utf-8 -*-

'''
Created on 13/03/2014

@author: DaGal
'''

from pygame.sprite import Group

class EntityGroup(Group):
	def __init__(self, *sprites):
		Group.__init__(self, *sprites)
	
	def update(self, time, collisionBg):
		for entity in self.sprites():
			entity.update(time, collisionBg)
	
	def draw(self, screen, camera):
		for entity in self.sprites():
			entity.draw(screen,camera)