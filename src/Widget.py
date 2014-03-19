
import pygame
from pygame import Rect

class Widget():
    
    def __init__(self, director, position = (0,0), size = (100,20), style = None, visible = True, parent = None):
                
        self.position = position
        self.size = size           
    
        self.visible = visible
        
        self.style = style
        
        self.mouseOver = False
        self.mouseButtons = []
        
        self.onMouseOver = None
        self.onMouseDown = None    
        
        self.parent = parent 
        self.director = director

        
    def processEvent(self, event):
        pass
    
    def update(self, time):
        self.checkMouseOver()
        self.checkMouseButtons()
        if self.mouseOver:
            if self.onMouseOver:
                self.onMouseOver()
            if self.mouseButtons[0]:
                if self.onMouseDown:
                    self.onMouseDown()

        
    def draw(self, surface):
        pass
    
    def getPosition(self):
        x = self.position[0]
        y = self.position[1]
        if self.parent != None:
            dx, dy = self.parent.getPosition()
            x = x + dx
            y = y + dy
        return (x, y)
    
    def checkMouseOver(self):
        x, y = self.getPosition()
        if Rect(x, y, self.size[0], self.size[1]).collidepoint(pygame.mouse.get_pos()):
            self.mouseOver = True
        else:
            self.mouseOver = False
            
    def checkMouseButtons(self):
        self.mouseButtons = pygame.mouse.get_pressed()
        