# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

from Resources import clearResources


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
