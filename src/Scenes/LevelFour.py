# -*- coding: utf-8 -*-


from Camera import *
from Level import Level
from Resources import *
import Constants
from Weapons.WpnLaser import WpnLaser
from Weapons.WpnBlade import WpnBlade
from Laser import Laser
from EntityGroup import EntityGroup
from Characters.FutureSoldier import FutureSoldier
from Characters.Page import Page
from InvisibleFloor import InvisibleFloor
from Events import *
from Scenes.MessageScene import MessageScene

import pygame


class LevelFour(Level):
    def __init__(self, director, player):
        Level.__init__(self, director, player)
        self.player.rect.x = 224
        self.player.rect.y = 1273

        self.laser0 = Laser(80, 340, 'laser_45.png')
        self.laser1 = Laser(400, 75, 'laser_45.png')
        self.laser2 = Laser(405, 332, 'laser_180.png')
        self.laser3 = Laser(80, 330, 'laser_180.png')
        self.laser4 = Laser(406, 341, 'laser_125.png')
        self.laser5 = Laser(80, 80, 'laser_125.png')
        self.laser6 = Laser(400, 350, 'laser_90.png')
        self.laserArray = [self.laser0, self.laser1, self.laser2, self.laser3, self.laser4, self.laser5, self.laser6]
        self.laserGroup = EntityGroup([])
        self.laserGroup.add(self.laser0, self.laser1, self.laser2, self.laser3, self.laser4, self.laser5, self.laser6)
        self.groups.append(self.laserGroup)
        self.laser0.active = False
        self.laser1.active = False
        self.activeLG = 1  # Pair of lasers active at a given time
        self.time = 0

        self.page = Page(408, 135, self.player, director)
        self.enemyGroup.add([FutureSoldier(141, 1084, self.player, director),
#                              FutureSoldier(316, 1084, self.player, director),
#                              FutureSoldier(141, 926, self.player, director),
                            FutureSoldier(316, 926, self.player, director),
                             FutureSoldier(686, 1260, self.player, director),
                             FutureSoldier(508, 988, self.player, director),
                             FutureSoldier(537, 1450, self.player, director),
                             self.page])

        self.bg = load_image("map_page_img.png", Constants.MAP_DIR)
        self.collisionBg = load_image("map_page_bg.png", Constants.BG_MAP_DIR)

        self.invisibleFloor = InvisibleFloor(384, 202, 59, 78)  # Invisible sprite, it functions as a trigger
        self.invisibleFloorG = EntityGroup([])
        self.invisibleFloorG.add(self.invisibleFloor)
        self.groups.append(self.invisibleFloorG)

        load_music("level_four.s3m")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        player.setWeapons([WpnBlade("lightsaber.png", -1, pygame.Rect(128, 77, 42, 42), "sthswng1.wav", 0.2), \
                          WpnLaser()])

    def change_lasers(self):
        # Changes activeLG
        # laser0 and laser1 -> activeLG = 1
        # laser2 and laser3 -> activeLG = 3
        # laser4 and laser5 -> activeLG = 5
        # laser6 -> activeLG = 6
        self.laserArray[self.activeLG - 1].active = True
        self.laserArray[self.activeLG].active = True
        if self.activeLG == 5:
            self.laserArray[self.activeLG + 1].active = False
            self.activeLG = 6
        elif self.activeLG == 6:
            self.laserArray[0].active = False
            self.laserArray[1].active = False
            self.activeLG = 1
        else:
            self.laserArray[self.activeLG + 1].active = False
            self.laserArray[self.activeLG + 2].active = False
            self.activeLG += 2

    def disconnect_lasers(self):
        for laser in self.laserArray:
            laser.active = False
        self.activeLG = 0


    def update(self, time):
        Level.update(self, time)
        self.time += time
        if self.activeLG != 0 and self.time > 1000:
            self.change_lasers()
            self.time = 0
        laser = pygame.sprite.spritecollideany(self.player, self.laserGroup, pygame.sprite.collide_mask)
        if laser != None and laser.active:
            self.player.hp = 0
        if len(pygame.sprite.spritecollide(self.player, self.invisibleFloorG, True, pygame.sprite.collide_rect)) == 1:
            print 'Floor'
            self.disconnect_lasers()
            self.page.rect.x = 414
            self.page.rect.y = 414


    def processEvent(self, event):
        if event.type == pygame.USEREVENT and event.code == PAGEDEAD:
            m = MessageScene(self.director, self, 'Congratulations', "You have completed the game!\nNow you're entitled \nto the 3D version.", "Press to quit")
            m.messageBox.button.onMouseDown = lambda: pygame.event.post(pygame.event.Event(pygame.QUIT))
            self.director.setScene(m)

        Level.processEvent(self, event)
