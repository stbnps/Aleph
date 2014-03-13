
import ImageButton
from Container import Container
import pygame
import Constants
import os
import Resources
import ContainerButton


def createHUDStyle(bgIimage):

    bgStyle = {} 
    bgStyle['bg'] = bgIimage

    
    return bgStyle 

'''
UNFINISHED
'''
class HUD(Container):
    def __init__(self, position, visible):
        bgStyle = createHUDStyle(Resources.load_image("HUD_bg.png"))
        Container.__init__(self, position, bgStyle, visible)
        buttonImage = Resources.load_image('active_button.png')
        objectImage = pygame.Surface((2,2))
        activeButtonStyle = ContainerButton.createContainerButtonStyle(buttonImage, objectImage, 78)
        self.leftButton = ImageButton.ImageButton((180, 15), activeButtonStyle)
        self.rightButton = ImageButton.ImageButton((542, 15), activeButtonStyle)
        Container.addWidget(self, self.leftButton)
        Container.addWidget(self, self.rightButton)
        self.hidden = False

                 
    def update(self, time):
        # check if it needs to be hidden
        Container.update(self, time)
    
    def draw(self, surface):
        if self.visible:
            surface.blit(self.style['bg'], self.position)
            Container.draw(self, surface)

            
            