# -*- coding: utf-8 -*-

from pygame import Rect
from Enemy import Enemy
from Weapons.WpnLaser import WpnLaser

class FutureSoldier(Enemy):
    def __init__(self, x, y, player, director):
        Enemy.__init__(self, x, y, "FutureSoldier.png", -1, "coordFutureSoldier.txt", [3, 3, 3, 3], player, director, (0, 10, 6, 10, 6, 4, 6, 8))
        self.setWeapon(WpnLaser())
        self.hp = 50
        
