import pygame
from Scene import Scene, Layer
from Player import Player
import MessageBox
import Resources
from Constants import SCREEN_W , SCREEN_H
import math



class MessageScene(Scene):
    def __init__(self, director, pausedScene, title='Warning!', message='Message', tooltip='Press here to continue'):
        Scene.__init__(self, director)
        self.bluredBackground = None
        self.b = 1
        self.pausedScene = pausedScene
        layer = Layer(director)
        backgroundImage = Resources.load_image("message_box.png")
        buttonImage = Resources.load_image("message_box_button.png")
        buttonWidth = 372
        style = MessageBox.createMessageBoxStyle(backgroundImage, buttonImage, buttonWidth)
        self.messageBox = MessageBox.MessageBox(self.director, (SCREEN_W / 2 - style['bg'].get_width() / 2, SCREEN_H / 2 - style['bg'].get_height() / 2), style, True)
        self.messageBox.button.onMouseDown = lambda: self.popScene()
        self.messageBox.title = title
        self.messageBox.message = message
        self.messageBox.tooltip = tooltip
        layer.append(self.messageBox)
        self.layers.append(layer)

    def set_message(self, text):
        self.messageBox.message = text

    def popScene(self):
        self.director.setScene(self.pausedScene)

    '''
    The teacher wont allow us the use of any "external library" so I tried to 
    implement a simple convolution, sadly it runs extremely slow
    '''
    def convolve(self, inputImage, kernel):
        inputArray = pygame.PixelArray(inputImage)
        kernelArray = pygame.PixelArray(kernel)
        outputImage = pygame.Surface(inputImage.get_size())
        outputArray = pygame.PixelArray(outputImage)

        sO = outputImage.get_size()
#         sI = inputImage.get_size()
        sK = kernel.get_size()
        kCenterX = math.ceil(sK[0] / 2);
        kCenterY = math.ceil(sK[1] / 2);

        for y in range(0, sO[1]):
            for x in range(0, sO[0]):

                for yK in range(0, sK[1]):
                    for xK in range(0, sK[0]):

                        yI = int(y - kCenterY + yK)
                        xI = int(x - kCenterX + xK)

                        if yI < 0 or yI > sO[1]:
                            continue


                        if xI < 0 or xI > sO[0]:
                            continue

                        outputArray[x][y] = outputArray[x][y] + inputArray[xI][yI] * kernelArray[xK][yK]

        del inputArray
        del outputArray
        del kernelArray

        return outputImage

    def blur(self, surface, factor):
        surface = pygame.transform.smoothscale(surface, (int(SCREEN_W / factor), int(SCREEN_H / factor)))
        surface = pygame.transform.smoothscale(surface, (SCREEN_W, SCREEN_H))
        return surface

    def draw(self, screen):
        s = pygame.Surface((SCREEN_W, SCREEN_H))
        self.pausedScene.draw(s)
        self.bluredBackground = self.blur(s, self.b)
        if self.b < 10:
            self.b = self.b + 0.1
        screen.blit(self.bluredBackground, (0, 0))
        Scene.draw(self, screen)
