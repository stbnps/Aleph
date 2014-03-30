# -*- coding: utf-8 -*-

from pygame import Rect
from Enemy import Enemy
from Weapons.WpnBlade import WpnBlade

class Centurion(Enemy):
    def __init__(self, x, y, player, director):
        Enemy.__init__(self, x, y, "centurion.png", -1, "coordCenturion.txt", [3, 3, 3, 3], player, (5, 25, 15, 25, 10, 25, 0, 30), director)
        self.setWeapon(WpnBlade("wpns2.png", -1, Rect(344, 342, 28, 28), "blade_swing.wav", 0.5))

        self.alive = True
        self.hp = 60

    def check_died(self, scene):
        Enemy.check_died(self, scene)
        if self.hp <= 0:
            scene.dead_sub_boss += 1
