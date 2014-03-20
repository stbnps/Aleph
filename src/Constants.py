# -*- coding: utf-8 -*-

import pygame


IMAGE_DIR = '../media/images/'
MAP_DIR = '../media/maps/compiled_maps/'
BG_MAP_DIR = '../media/maps/background_maps/'
SPRITES_DIR = "../media/sprites/"
FONTS_DIR = "../media/fonts/"


SCREEN_W = 800
SCREEN_H = 600

FONT_COLOR = (0, 255, 0)


DOWN = pygame.K_s
UP = pygame.K_w
LEFT = pygame.K_a
RIGHT = pygame.K_d

POS_UP = 0
POS_RIGHT = 1
POS_DOWN = 2
POS_LEFT = 3
POS_NUM = 4

TIME_TO_ROTATE_POS = 50

PLAYER_ATTACK_SPEED = 1.0 / 360.0
ENEMY_ATTACK_SPEED = 1.0 / 720.0
BLADE_SWING_ANGLE = 90

BOW_COOLDOWN = 500