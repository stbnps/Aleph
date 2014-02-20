# -*- encoding: utf-8 -*-

import pygame
from pygame.locals import *
from personajes import load_image
from escena import *

class PantallaInicial(Escena):

    def __init__(self, director):
        # Llamamos al constructor de la clase padre
        Escena.__init__(self, director);

        # La imagen de fondo
        self.imagen = load_image('portada.jpg')
        self.imagen = pygame.transform.scale(self.imagen, (ANCHO_PANTALLA, ALTO_PANTALLA))

        # El tipo de letra a utilizar
        self.tipoLetra = pygame.font.SysFont('arial', 32)


    def update(self, *args):
        return

    def evento(self, event):

        if event.type == KEYDOWN:
            teclasPulsadas = pygame.key.get_pressed()
            if teclasPulsadas[K_ESCAPE]:
                self.director.salirPrograma()
            else:
                self.director.salirEscena()

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.imagen.get_rect())
        pantalla.blit(self.tipoLetra.render('Pulse cualquier tecla para comenzar, o ESC para salir', True, (0, 255, 255)), (20, ALTO_PANTALLA-50, 200, 100))

