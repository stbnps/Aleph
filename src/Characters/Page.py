# -*- coding: utf-8 -*-

from pygame import Rect, event, USEREVENT
from Enemy import Enemy
from Weapons.WpnBlade import WpnBlade
from Events import *

class Page(Enemy):
    def __init__(self, x, y, player, director):
        Enemy.__init__(self, x, y, "page.png", -1, "coordLarryPage.txt", [3, 3, 3, 3], player, (0, 10, 6, 10, 2, 4, 6, 11), director)
        self.setWeapon(WpnBlade("lightsaber.png", -1, Rect(128, 209, 42, 42), "sthswng1.wav", 0.2))
        self.hp = 300

    def check_died(self, scene):
        """
        Check whether this enemy has died.
        """
        if self.hp <= 0:
            scene.enemyGroup.remove(self)
            event.post(event.Event(USEREVENT, code=PAGEDEAD))