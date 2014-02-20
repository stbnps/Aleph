# -*- encoding: utf-8 -*-

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# -------------------------------------------------
# Clase Escena con lo metodos abstractos

class Escena:

    def __init__(self, director):
        self.director = director

    def update(self, *args):
        raise NotImplemented("Tiene que implementar el metodo update.")

    def evento(self, *args):
        raise NotImplemented("Tiene que implementar el metodo evento.")

    def dibujar(self, pantalla):
        raise NotImplemented("Tiene que implementar el metodo dibujar.")
