
import pygame
from pygame import Rect

class Widget():
    
    def __init__(self, position = (0,0), size = (100,20), style = None, visible = True):
                
        self.position = position
        self.size = size           
    
        self.visible = visible
        
        self.style = style
        
        self.mouseOver = False
        self.mouseButtons = []
        
        self.onMouseOver = None
        self.onMouseDown = None     

        
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
    
    def checkMouseOver(self):
        if Rect(self.position[0], self.position[1], self.size[0], self.size[1]).collidepoint(pygame.mouse.get_pos()):
            self.mouseOver = True
        else:
            self.mouseOver = False
            
    def checkMouseButtons(self):
        self.mouseButtons = pygame.mouse.get_pressed()
        