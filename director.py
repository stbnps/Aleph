# -*- encoding: utf-8 -*-

# Modulos
import pygame
import sys
#import escena
from escena import *
from pygame.locals import *


class Director():

    def __init__(self):
        # Inicializamos la pantalla y el modografico
        self.screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pygame.display.set_caption("Juego con escenas")
        # Escena actual
        self.escena = None
        # Flag que nos indica cuando quieren salir de la escena o del programa
        self.salir_escena = False
        self.salir_programa = False
        # Reloj
        self.reloj = pygame.time.Clock()

    def bucle(self):

        # El bucle del juego, las acciones que se realicen se harán en cada escena
        while not self.salir_escena and not self.salir_programa:

            # Sincronizar el juego a 60 fps
            tiempo_pasado = self.reloj.tick(60)
            
            # Para cada evento
            for event in pygame.event.get():

                # Si se sale del programa
                if event.type == pygame.QUIT:
                    self.salirPrograma()

                # Realizamos los eventos
                self.escena.evento(event)


            # Actualiza la escena y nos dice si hay que terminar
            self.escena.update(tiempo_pasado)

            # Se dibuja en pantalla
            self.escena.dibujar(self.screen)
            pygame.display.flip()

        # Al final se devuelve si se quiere salir del programa, ademas de salir de la escena
        return self.salir_programa

    def cambiarEscena(self, escena):
        self.salir_escena = False
        self.programa_escena = False
        self.escena = escena

    def salirEscena(self):
        self.salir_escena = True

    def salirPrograma(self):
        self.salir_programa = True
