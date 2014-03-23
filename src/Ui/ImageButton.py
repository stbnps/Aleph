
from pygame import Rect
from Widget import Widget

def createImageButtonStyle(image, buttonWidth):
    if image.get_width() < buttonWidth:
        raise Exception("The button width must be less or equal than image width.")
    
    style = {}
        
    h = image.get_height()
    
    style['image-normal'] = image.subsurface(Rect(0,0,buttonWidth,h))
    
    if image.get_width() >= buttonWidth * 2:
        style['do-over'] = True
        style['image-over'] = image.subsurface(Rect(buttonWidth,0,buttonWidth,h))
    else:
        style['do-over'] = False
    
    if image.get_width() >= buttonWidth * 3:
        style['do-down'] = True
        style['image-down'] = image.subsurface(Rect(buttonWidth*2,0,buttonWidth,h))
    else:
        style['do-down'] = False
    
    if image.get_width() >= buttonWidth * 4:
        style['do-disabled'] = True
        style['image-disabled'] = image.subsurface(Rect(buttonWidth*3,0,buttonWidth,h))
    else:
        style['do-disabled'] = False
    
    return style  


class ImageButton(Widget):      
    def __init__(self, director, position = (0,0), style = None, visible = True):
        
        Widget.__init__(self, director, position, style['image-normal'].get_size(), style, visible)

    
    def draw(self, surface):
        if self.visible:
            if self.mouseButtons[0] and self.style['do-down']:
                suffix = "-down"
            elif self.mouseOver and self.style['do-over']:
                suffix = "-over"
            else:
                suffix = "-normal"
            
            surface.blit(self.style['image' + suffix], self.getPosition())
            