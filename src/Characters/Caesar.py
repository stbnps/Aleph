# -*- coding: utf-8 -*-

from pygame import Rect
from Enemy import Enemy
from Scenes.MessageScene import MessageScene
from Weapons.WpnBlade import WpnBlade

class Caesar(Enemy):
    def __init__(self, x, y, player, director):
        Enemy.__init__(self, x, y, "caesar.png", -1, "coordCaesar.txt", [3, 3, 3, 3], player, director, (0, 10, 6, 10, 2, 4, 6, 11))
        self.setWeapon(WpnBlade("wpns2.png", -1, Rect(344, 342, 28, 28), "blade_swing.wav", 0.5))
        self.hp = 60
