# -*- coding: utf-8 -*-

'''
Created on 16/03/2014

@author: DaGal
'''

from Enemy import Enemy
from Weapons.WpnRifle import WpnRifle


class Mr_H(Enemy):

    def __init__(self, x, y, player):
        Enemy.__init__(self, x, y, "mr_h.png", -1, "coordMr_h.txt", [
                       3, 3, 3, 3], player, (0, 10, 6, 10, 6, 4, 6, 8))

        # Maybe another kind of weapon?
        self.setWeapon(WpnRifle())
