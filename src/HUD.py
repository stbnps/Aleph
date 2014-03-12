
import ImageButton
from Container import Container
import pygame
import Constants
import os
import Util


def createHUDStyle(bgIimage):

    bgStyle = {} 
    bgStyle['bg'] = bgIimage

    
    return bgStyle 

'''
UNFINISHED
'''
class HUD(Container):
    def __init__(self, position, visible):
        style = createHUDStyle(Util.load_image("HUD.png"))
        Container.__init__(self, position, style, visible)
        self.button = ImageButton.ImageButton((14, 248), style)
        Container.addWidget(self, self.button)
        self.title = 'title'
        self.message = 'message'
        self.tooltip = 'tooltip'
        fullname = os.path.join(Constants.FONTS_DIR , 'neuropolitical.ttf')
        self.titleFont = pygame.font.Font(fullname, 19)
        self.textFont = pygame.font.Font(fullname, 16)
        self.tooltipFont = pygame.font.Font(fullname, 14)
        
    def printTitle(self, text, surface):
        text = self.titleFont.render(text, True, Constants.FONT_COLOR)
        textRect = text.get_rect()
        textRect.centerx = self.getPosition()[0] + self.size[0] / 2
        textRect.centery = self.getPosition()[1] + 20
        surface.blit(text, textRect)
        
    def printContent(self, text, surface):
        offset = self.getPosition()[1] + 80
        step = 20
        lines = text.splitlines()
        for line in lines:            
            text = self.textFont.render(line, True, Constants.FONT_COLOR)
            textRect = text.get_rect()
            textRect[0] = self.getPosition()[0] + self.size[0] / 8
            textRect.centery = offset
            surface.blit(text, textRect)
            offset = offset + step
            
    def printTooltip(self, text, surface):
        text = self.tooltipFont.render(text, True, Constants.FONT_COLOR)
        textRect = text.get_rect()
        textRect.centerx = self.getPosition()[0] + self.size[0] / 2
        textRect.centery = self.getPosition()[1] + 270
        surface.blit(text, textRect)
                 
    def draw(self, surface):
        if self.visible:
            surface.blit(self.style['bg'], self.position)
            Container.draw(self, surface)
            
            self.printTitle("Warning!", surface)
            self.printContent("Reach the portal\nbefore you die!", surface)
            self.printTooltip("Press here to continue", surface)
            
            