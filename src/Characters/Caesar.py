# -*- coding: utf-8 -*-

from pygame import Rect, event, USEREVENT
from Enemy import Enemy
from Scenes.MessageScene import MessageScene
from Weapons.WpnBlade import WpnBlade
from Events import *

class Caesar(Enemy):
    def __init__(self, x, y, player, director):
        Enemy.__init__(self, x, y, "caesar.png", -1, "coordCaesar.txt", [3, 3, 3, 3], player, (0, 10, 6, 10, 2, 4, 6, 11), director)
        self.setWeapon(WpnBlade("wpns2.png", -1, Rect(344, 342, 28, 28), "blade_swing.wav", 0.5))
        self.hp = 60

    def check_died(self, scene):
        """
        Check whether this enemy has died.
        """
        if self.hp <= 0:
            scene.enemyGroup.remove(self)
            event.post(event.Event(USEREVENT, code=CAESARDEAD))
