# -*- coding: utf-8 -*-

import pygame, escena
from escena import *
from personajes import *
from pygame.locals import *

# -------------------------------------------------
# -------------------------------------------------
# Constantes
# -------------------------------------------------
# -------------------------------------------------

VELOCIDAD_SOL = 0.1 # Pixeles por milisegundo


MINIMO_X_JUGADOR = 50
MAXIMO_X_JUGADOR = ANCHO_PANTALLA - 100

# -------------------------------------------------
# Clase Fase

class Fase(Escena):
    def __init__(self, director, jugador1, jugador2):

        # Primero invocamos al constructor de la clase padre
        Escena.__init__(self, director)

        # Guardamos los jugadores
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.grupoJugadores = pygame.sprite.Group( jugador1, jugador2 )

        # Ponemos a los jugadores en sus posiciones iniciales
        jugador1.establecerPosicion(200, 551)
        jugador2.establecerPosicion(400, 551)

        # Habria que pasarle como parámetro el número de fase, a partir del cual se cargue
        #  un fichero donde este la configuracion de esa fase en concreto, con cosas como
        #   - Nombre del archivo con el decorado
        #   - Posiciones de las plataformas
        #   - Posiciones de los enemigos
        #   - Posiciones de inicio de los jugadores
        #  etc.
        # Y cargar esa configuracion del archivo en lugar de ponerla a mano, como aqui abajo
        # De esta forma, se podrian tener muchas fases distintas con esta clase

        # Cargamos el decorado
        self.image = load_image('decorado.png', -1)
        self.image = pygame.transform.scale(self.image, (1200, 300))

        self.rect = self.image.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        # Creamos el fondo
        self.sol = Fondo('sol.png')

        # Que parte del decorado estamos visualizando
        self.posicionx = 0
        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        self.rectSubimagen.left = self.posicionx

        # Creamos las plataformas del decorado
        # La plataforma que conforma todo el suelo
        plataformaSuelo = Plataforma(pygame.Rect(0, 550, 1200, 15))
        # La plataforma del techo del edificio
        plataformaCasa = Plataforma(pygame.Rect(870, 417, 200, 10))
        # y el grupo con las mismas
        self.grupoPlataformas = pygame.sprite.Group( plataformaSuelo, plataformaCasa )

        # Y los enemigos que tendran en este decorado
        enemigo1 = Sniper()
        enemigo1.establecerPosicion(1000, 418)

        # Creamos un grupo con los enemigos
        self.grupoEnemigos = pygame.sprite.Group( enemigo1 )

    def posicionesInicioJugadores(self):
        return self.inicioJugador1, self.inicioJugador2

    # Desplaza todo el decorado y los objetos (plataformas, enemigos) que hay en el
    def desplazarDecorado(self, desplazamiento, jugadorAMover):
        # Desplazamos el jugador a mover hacia el lado contrario
        jugadorAMover.posicionx -= desplazamiento
        jugadorAMover.rect.left = jugadorAMover.posicionx
        # La imagen que se muestra hacia ese lado
        self.posicionx += desplazamiento

        # Actualizamos el grupo de plataformas para que tambien se desplacen al lado contrario
        self.grupoPlataformas.update(-desplazamiento)

        # Actualizamos el grupo de enemigos para que tambien se desplacen al lado contrario
        for enemigo in list(self.grupoEnemigos):
            enemigo.posicionx -= desplazamiento
            enemigo.rect.left = enemigo.posicionx

        # Actualizamos cual es la parte de la imagen del decorado que se muestra en pantalla
        self.rectSubimagen.left = self.posicionx

        
    def actualizarScrollOrdenados(self, jugadorIzq, jugadorDcha):
        if (jugadorIzq.posicionx<=MINIMO_X_JUGADOR) and (jugadorDcha.posicionx>=MAXIMO_X_JUGADOR):
            jugadorIzq.posicionx = MINIMO_X_JUGADOR
            jugadorDcha.posicionx = MAXIMO_X_JUGADOR
            return
        # Si el jugador de la izquierda quiere moverse mas a la izquierda
        if (jugadorIzq.posicionx<MINIMO_X_JUGADOR):
            desplazamiento = MINIMO_X_JUGADOR - jugadorIzq.posicionx
            jugadorIzq.posicionx = MINIMO_X_JUGADOR

            # Si el escenario ya está a la izquierda del todo, no lo movemos mas
            if self.posicionx <= 0:
                self.posicionx = 0

            # Si se puede hacer scroll a la izquierda
            else:
                # Desplazamos todo el decorado a la izquierda, incluyendo el jugador que este en la derecha
                self.desplazarDecorado(-desplazamiento, jugadorDcha)

        # Si el jugador de la derecha quiere moverse mas a la derecha
        if (jugadorDcha.posicionx>MAXIMO_X_JUGADOR):
            desplazamiento = jugadorDcha.posicionx - MAXIMO_X_JUGADOR
            jugadorDcha.posicionx = MAXIMO_X_JUGADOR

            # Si el escenario ya está a la derecha del todo, no lo movemos mas
            if self.posicionx + ANCHO_PANTALLA >= self.image.get_rect().right:
                self.posicionx = self.image.get_rect().right - ANCHO_PANTALLA

            # Si se puede hacer scroll a la derecha
            else:
                # Desplazamos todo el decorado a la derecha, incluyendo el jugador que este en la izquierda
                self.desplazarDecorado(desplazamiento, jugadorIzq)



    def actualizarScroll(self, jugador1, jugador2):
        if (jugador1.posicionx<jugador2.posicionx):
            return self.actualizarScrollOrdenados(jugador1, jugador2)
        else:
            return self.actualizarScrollOrdenados(jugador2, jugador1)

    # Se actualiza el decorado, realizando las siguientes acciones:
    #  Se actualizan los jugadores con los movimientos a realizar
    #  Se actualiza la posicion del sol y el color del cielo
    #  Se mueven los enemigos como sea conveniente
    #  Se comprueba si hay colision entre algun jugador y algun enemigo
    #  Se actualiza el scroll del decorado y los objetos en el
    def update(self, tiempo):

        # Actualizamos los jugadores actualizando el grupo
        self.grupoJugadores.update(self.grupoPlataformas, tiempo)
        # Actualizamos la posicion del sol y el color del cielo
        self.sol.update(tiempo)
        # Indicamos la accion a realizar para cada enemigo segun como esten los jugadores
        for enemigo in iter(self.grupoEnemigos):
            enemigo.mover_cpu(self.jugador1, self.jugador2)
        #  y la realizamos
        self.grupoEnemigos.update(self.grupoPlataformas, tiempo)
        # Comprobamos si hay colision entre algun jugador y algun enemigo
        # Si la hay, le indicamos al director que se ha finalizado esa escena
        if pygame.sprite.spritecollideany(self.jugador1, self.grupoEnemigos) != None:
            self.director.salirEscena()
        if pygame.sprite.spritecollideany(self.jugador2, self.grupoEnemigos) != None:
            self.director.salirEscena()
        # Actualizamos el scroll
        self.actualizarScroll(self.jugador1, self.jugador2)


        
    def dibujar(self, pantalla):
        # Ponemos primero el sol y cielo
        self.sol.dibujar(pantalla)
        # Después la imagen de fondo
        pantalla.blit(self.image, self.rect, self.rectSubimagen)
        # Luego los enemigos
        self.grupoEnemigos.draw(pantalla)
        # Por ultimo, los jugadores
        self.grupoJugadores.draw(pantalla)


    def evento(self, event):
        # Indicamos la acción a realizar segun la tecla pulsada para cada jugador
        teclasPulsadas = pygame.key.get_pressed()
        self.jugador1.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.jugador2.mover(teclasPulsadas, K_w,  K_s,    K_a,    K_d)

# -------------------------------------------------
# Clase Plataforma

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,rectangulo):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self);
        # Rectangulo con las coordenadas que ocupara
        self.rect = rectangulo
        # Posicion en el eje x (en el eje y no hace falta, no hay scroll vertical)
        self.posx = self.rect.left

        # En el caso particular de este juego, las plataformas no se van a ver, asi que no se carga ninguna imagen
        self.image = None


    def update(self,desplazamiento):
        self.posx += desplazamiento
        self.rect.left = self.posx


# -------------------------------------------------
# Clase Fondo

class Fondo(pygame.sprite.Sprite):
    def __init__(self,nombreImagen):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self);

        self.image = load_image(nombreImagen,-1)
        self.image = pygame.transform.scale(self.image, (300, 200))

        self.rect = self.image.get_rect()
        self.posicionx = 0 # El lado izquierdo de la subimagen que se esta visualizando
        self.update(0)

    def update(self, tiempo):
        self.posicionx += VELOCIDAD_SOL * tiempo
        if (self.posicionx - self.rect.width >= ANCHO_PANTALLA):
            self.posicionx = 0
        self.rect.right = self.posicionx
        # Calculamos el color del cielo
        if self.posicionx >= ((self.rect.width + ANCHO_PANTALLA) / 2):
            ratio = 2 * ((self.rect.width + ANCHO_PANTALLA) - self.posicionx) / (self.rect.width + ANCHO_PANTALLA)
        else:
            ratio = 2 * self.posicionx / (self.rect.width + ANCHO_PANTALLA)
        self.colorCielo = (100*ratio, 200*ratio, 255)
        
    def dibujar(self,pantalla):
        # Dibujamos el color del cielo
        pantalla.fill(self.colorCielo)
        # Y ponemos el sol
        pantalla.blit(self.image, self.rect)


