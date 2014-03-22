
from pygame import Rect
from Widget import Widget


class Container(Widget):

    def __init__(self,  director, position=(0, 0), style = None, visible = True):
        Widget.__init__(self, director, position,
                        style['bg'].get_size(), style, visible)
        self.widgets = []

    def addWidget(self, widget):
        widget.parent = self
        self.widgets.append(widget)

    def removeWidget(self, widget):
        self.widgets.remove(widget)

    def update(self, time):
        Widget.update(self, time)
        for w in self.widgets:
            w.update(time)

    def draw(self, surface):
        if self.visible:
# subSurface = surface.subsurface(Rect(self.position[0], self.position[1],
# self.size[0], self.size[1])) # Draw them relative to the containers
# location
            for w in self.widgets:
                w.draw(surface)
