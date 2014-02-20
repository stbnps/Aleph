#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importar modulos
import pygame
import director
import fase
from director import *
from fase import *
from inicial import *


class AplicacionJuego():

    def __init__(self):
        # Inicializamos la libreria de pygame
        pygame.init()
        # Creamos el director
        self.director = Director()

    def ejecutar(self):

        while True:

            # Creamos la escena con la pantalla inicial
            escena = PantallaInicial(self.director)
            # Le decimos al director en que escena estamos
            self.director.cambiarEscena(escena)
            # Y ejecutamos el bucle
            salir_programa = self.director.bucle()
            if (salir_programa):
                # Si ademas de salir de la escena, se quiere salir del programa, se finaliza
                pygame.quit()
                sys.exit()

            # En este punto, hay que iniciar el juego en sí
       
            # Creamos los jugadores
            jugador1 = Jugador()
            #jugador2 = Jugador()

            # Creamos la escena con la fase
            #escena = Fase(self.director, jugador1, jugador2)
            escena = Fase(self.director, jugador1)
            # Le decimos al director en que escena estamos
            self.director.cambiarEscena(escena)
            # Y ejecutamos el bucle
            salir_programa = self.director.bucle()
            if (salir_programa):
                # Si ademas de salir de la escena, se quiere salir del programa, se finaliza
                pygame.quit()
                sys.exit()



if __name__ == '__main__':
    juego = AplicacionJuego()
    juego.ejecutar()
