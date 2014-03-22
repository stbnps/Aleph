# -*- coding: utf-8 -*-
'''
Collection of objects that will be drawn at the "same" Z level
'''


class Layer():

    def __init__(self, director):
        self.director = director
        self.components = []

    def append(self, o):
        self.components.append(o)

    def update(self, time):
        for c in self.components:
            c.update(time)

    def processEvent(self, event):
        for c in self.components:
            c.processEvent(event)

    def draw(self, screen):
        for c in self.components:
            c.draw(screen)
