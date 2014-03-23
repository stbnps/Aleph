# -*- coding: utf-8 -*-

'''
Created on 15/03/2014

@author: DaGal
'''

import pygame
from Scene import Scene 
from Layer import Layer
from MessageScene import MessageScene
from EntityGroup import EntityGroup
from Camera import Camera
from Ui.HUD import HUD


class Level(Scene):

    def __init__(self, director, player):
        Scene.__init__(self, director)
        self.player = player
        self.enemyGroup = EntityGroup([])
        self.bulletGroup = EntityGroup([])
        self.groups = []
        self.groups.append(self.enemyGroup)
        self.groups.append(self.bulletGroup)

        self.bg = None
        self.collisionBg = None
        self.camera = Camera()

        self.HUD = HUD(self.director, (0, 467), True, player)
        hudLayer = Layer(self.director)
        hudLayer.append(self.HUD)
        self.layers.append(hudLayer)
        self.mouseHoveringHUD = False

    def update(self, time):
        Scene.update(self, time)

        if self.collisionBg != None:
            self.player.update(time, self)
            for group in self.groups:
                group.update(time, self)

        self.camera.update(self.player)

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            m = MessageScene(self.director, self)
            self.director.setScene(m)

        self.player.controller.processEvent(event)
        Scene.processEvent(self, event)

    def draw(self, screen):
        screen.fill(0x000000)

        if self.bg:
            screen.blit(self.bg, self.camera.state)

        self.player.draw(screen, self.camera)
        for group in self.groups:
            group.draw(screen, self.camera)
        # TODO: move maps and characters to its own layer
        Scene.draw(self, screen)  # draws rest of layers

    def game_over(self):
        """ Called when the player dies.
        """
        game_over_scene = MessageScene(self.director, self)
        game_over_scene.set_message("Has Muerto.")
        self.director.setScene(game_over_scene)
