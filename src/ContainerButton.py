
from pygame import Rect
from Widget import Widget
from ImageButton import ImageButton, createImageButtonStyle

def createContainerButtonStyle(buttonImage, objectImage, buttonWidth):
    
    objStyle = {} 
    objStyle['obj'] = objectImage
    
    buttonStyle = createImageButtonStyle(buttonImage, buttonWidth)
    
    style = dict(objStyle.items() + buttonStyle.items())    
    
    return style  


class ContainerButton(ImageButton):      
    def __init__(self, director, position = (0,0), style = None, visible = True):
        
        ImageButton.__init__(self, director, position, style, visible)

    
    def draw(self, surface):
        if self.visible:
            ImageButton.draw(self, surface)
            surface.blit(self.style['obj'], self.getPosition())
            