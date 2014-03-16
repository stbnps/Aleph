
import pygame
from Scene import Scene, Layer
from Player import Player
import ImageButton
from Resources import load_image
from WpnBlade import WpnBlade
from WpnBow import WpnBow
from WpnRifle import WpnRifle
from WpnLaser import WpnLaser
from LevelTwo import LevelTwo


class MainMenu(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        layer = Layer(director)
        self.backgroundImage = load_image("main_menu_background.png")
        self.leftCoverImage = load_image("left_cover.png")
        newGameImage = load_image("new_game.png")
        buttonWidth = 214
        style = ImageButton.createImageButtonStyle(newGameImage, buttonWidth)
        self.newGameButton = ImageButton.ImageButton((60, 110), style)
        # Next Scene, we could do just self.newGameButton.onMouseDown = self.loadNewGame
        # put this way loadNewGame can take parameters too
        self.newGameButton.onMouseDown = lambda: self.loadNewGame()
        layer.append(self.newGameButton)

        self.layers.append(layer)

    def loadNewGame(self):
        player = Player(200, 200)
        # player.setWeapon(WpnBlade("lightsaber.png", -1, pygame.Rect(128, 77, 42, 42)))
        # player.setWeapon(WpnBow("items-1.png", None, pygame.Rect(0, 24, 24, 24)))
        # player.setWeapon(WpnRifle())
        player.setWeapon(WpnLaser())
        scene = LevelTwo(self.director, player)
        self.director.setScene(scene)

    def draw(self, surface):
        surface.blit(self.backgroundImage, (0, 0))
        surface.blit(self.leftCoverImage, (0, 0))
        Scene.draw(self, surface)
