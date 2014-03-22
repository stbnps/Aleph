
import ImageButton
from Container import Container
import pygame
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

    def __init__(self, director, position, visible, player=None):
        bgStyle = createHUDStyle(Resources.load_image("HUD_bg.png"))
        Container.__init__(self, director, position, bgStyle, visible)
        buttonImage = Resources.load_image('active_button.png')
        objectImage = pygame.Surface((2, 2))
        activeButtonStyle = ContainerButton.createContainerButtonStyle(
            buttonImage, objectImage, 78)
        self.leftButton = ImageButton.ImageButton(
            self.director, (180, 15), activeButtonStyle)
        self.rightButton = ImageButton.ImageButton(
            self.director, (542, 15), activeButtonStyle)
        Container.addWidget(self, self.leftButton)
        Container.addWidget(self, self.rightButton)
        self.hidden = True
        self.player = player
        self.originalPosition = self.position
        self.lastEvent = None
        self.newEvent = False

    def drawBars(self, ammount, initialColor, colorDecay):
        healthSurface = pygame.Surface((150, 60), pygame.SRCALPHA, 32)
        barCount = int(ammount * 1.5)
        color = initialColor
        for pos in range(0, barCount, 6):
            color = (color[0] + colorDecay[0], color[
                     1] + colorDecay[1], color[2] + colorDecay[2])
            p = int(pos / 3.6)
            pygame.draw.rect(healthSurface, color, (pos, 45 - p, 3, 10 + p))
        return healthSurface

    def drawHealth(self, ammount, surface):
        if ammount > 100:
            ammount = 100
        if ammount < 0:
            ammount = 0
        healthSurface = self.drawBars(ammount, (225, 128, 0), (0, -4, 0))
        surface.blit(
            healthSurface, (self.getPosition()[0] + 20, self.getPosition()[1] + 65))

    def drawAmmo(self, ammount, surface):
        if ammount > 100:
            ammount = 100
        if ammount < 0:
            ammount = 0
        armorSurface = self.drawBars(ammount, (128, 150, 255), (-4, -1, 0))
        armorSurface = pygame.transform.flip(armorSurface, True, False)
        surface.blit(
            armorSurface, (self.getPosition()[0] + 630, self.getPosition()[1] + 65))

    def drawItems(self, surface):
        pass

    def processEvent(self, event):
        self.newEvent = True
        self.lastEvent = event

    def checkHide(self):
        if self.mouseOver and self.newEvent and self.lastEvent.type == pygame.MOUSEBUTTONUP:
            self.newEvent = False
            overCount = 0
            for w in self.widgets:
                if w.mouseOver:
                    overCount += 1

            if overCount == 0:
                self.hidden = not self.hidden

    def update(self, time):
        # check if it needs to be hidden
        self.checkHide()
        if self.hidden:
            if self.position[1] < 580:
                self.position = (self.position[0], self.position[1] + 5)
            else:
                self.position = (self.position[0], 580)
        else:
            if self.position[1] > self.originalPosition[1]:
                self.position = (self.position[0], self.position[1] - 5)
            else:
                self.position = self.originalPosition

        Container.update(self, time)

        '''
        Yes, this is a nasty hack. We don't have time for refactoring
        '''
        if self.mouseOver:
            self.director.scene.mouseHoveringHUD = True
        else:
            self.director.scene.mouseHoveringHUD = False

    def draw(self, surface):
        if self.visible:
            surface.blit(self.style['bg'], self.position)
            Container.draw(self, surface)
            self.drawHealth(self.player.hp * 2, surface)
            self.drawAmmo((self.player.hp - 50) * 2, surface)
            self.drawItems(surface)
