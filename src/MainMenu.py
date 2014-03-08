
import pygame
from Scene import Scene, Layer
from GameScene import GameScene
from Player import Player
from Enemy import Enemy
import ImageButton
import Util


class MainMenu(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        layer = Layer(director)
        self.backgroundImage = Util.load_image("main_menu_background.png")
        self.leftCoverImage = Util.load_image("left_cover.png")
        newGameImage = Util.load_image("new_game.png")
        buttonWidth = 214
        style = ImageButton.createImageButtonStyle(newGameImage, buttonWidth)
        self.newGameButton = ImageButton.ImageButton((60, 110), style)
        # Next Scene, we could do just self.newGameButton.onMouseDown = self.loadNewGame
        # put this way loadNewGame can take parameters too
        self.newGameButton.onMouseDown = lambda: self.loadNewGame()
        layer.append(self.newGameButton)

        self.layers.append(layer)

    def loadNewGame(self):
        player = Player(200, 200, "player-alt.png", -1, "coordPlayerAlt2.txt", [3, 3, 3, 3])
        enemy = Enemy(300, 250, "player-alt.png", -1, "coordPlayerAlt2.txt", [3, 3, 3, 3], player)
        scene = GameScene(self.director, player, enemy)
        self.director.setScene(scene)

    def draw(self, surface):
        surface.blit(self.backgroundImage, (0, 0))
        surface.blit(self.leftCoverImage, (0, 0))
        Scene.draw(self, surface)
