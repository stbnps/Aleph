# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from escena import *

# -------------------------------------------------
# -------------------------------------------------
# Constantes
# -------------------------------------------------
# -------------------------------------------------

# Movimientos
QUIETO = 0
IZQUIERDA = 1
DERECHA = 2
ARRIBA = 3
ABAJO = 4

#Posturas
SPRITE_QUIETO = 0
SPRITE_ANDANDO = 1
SPRITE_SALTANDO = 2

# Velocidades de los distintos personajes
VELOCIDAD_JUGADOR = 0.2 # Pixeles por milisegundo
VELOCIDAD_SALTO_JUGADOR = 0.3 # Pixeles por milisegundo
RETARDO_ANIMACION_JUGADOR = 1 / VELOCIDAD_JUGADOR

VELOCIDAD_SNIPER = 0.12 # Pixeles por milisegundo
VELOCIDAD_SALTO_SNIPER = 0.27 # Pixeles por milisegundo
RETARDO_ANIMACION_SNIPER = 1 / VELOCIDAD_SNIPER
# El Sniper camina un poco más lento que el jugador, y salta menos


# -------------------------------------------------
# -------------------------------------------------
# Funciones auxiliares
# -------------------------------------------------
# -------------------------------------------------

# El colorkey es es color que indicara la transparencia
#  Si no se usa, no habra transparencia
#  Si se especifica -1, el color de transparencia sera el del pixel (0,0)
#  Si se especifica un color, ese sera la transparencia
def load_image(name, colorkey=None):
    fullname = os.path.join('imagenes', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

# -------------------------------------------------
# -------------------------------------------------
# Clases de los objetos del juego
# -------------------------------------------------
# -------------------------------------------------


# -------------------------------------------------
# Clases Personaje

class Personaje(pygame.sprite.Sprite):
    "Cualquier personaje del juego"

    # Parametros pasados al constructor de esta clase:
    #  Posicion que ocupa el personaje
    #  Archivo con la hoja de Sprites
    #  Archivo con las coordenadoas dentro de la hoja
    #  Numero de imagenes en cada postura
    #  Velocidad de caminar y de salto
    #  Retardo para mostrar la animacion del personaje
    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidad, velocidadSalto, retardoAnimacion):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self);
        # Se carga la hoja
        self.hoja = load_image(archivoImagen,-1)
        self.hoja = self.hoja.convert_alpha()
        # El movimiento que esta realizando
        self.movimiento = QUIETO
        # Lado hacia el que esta mirando
        self.mirando = IZQUIERDA

        # Leemos las coordenadas de un archivo de texto
        fullname = os.path.join('imagenes', archivoCoordenadas)
        pfile=open(fullname,'r')
        datos=pfile.read()
        pfile.close()
        datos = datos.split()
        self.numPostura = 1;
        self.numImagenPostura = 0;
        cont = 0;
        self.coordenadasHoja = [];
        for linea in range(0, 3):
            self.coordenadasHoja.append([])
            tmp = self.coordenadasHoja[linea]
            for postura in range(1, numImagenes[linea]+1):
                tmp.append(pygame.Rect((int(datos[cont]), int(datos[cont+1])), (int(datos[cont+2]), int(datos[cont+3]))))
                cont += 4

        # El retardo a la hora de cambiar la imagen del Sprite (para que no se mueva demasiado rápido)
        self.retardoMovimiento = 0;

        # En que postura esta inicialmente
        self.numPostura = QUIETO

        # El rectangulo del Sprite
        self.rect = pygame.Rect(100,100,self.coordenadasHoja[self.numPostura][self.numImagenPostura][2],self.coordenadasHoja[self.numPostura][self.numImagenPostura][3])

        # La posicion x e y que ocupa
        self.posicionx = 0
        self.posiciony = 0
        self.rect.left = 0
        self.rect.bottom = 0
        # Velocidad en el eje y (para los saltos)
        #  En el eje x se utilizaria si hubiese algun tipo de inercia
        self.velocidady = 0

        # Las velocidades de caminar y salto
        self.velocidad = velocidad
        self.velocidadSalto = velocidadSalto

        # El retardo en la animacion del personaje (podria y deberia ser distinto para cada postura)
        self.retardoAnimacion = retardoAnimacion

        # Y actualizamos la postura del Sprite inicial, llamando al metodo correspondiente
        self.actualizarPostura()


    def establecerPosicion(self, posicionx, posiciony):
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.rect.left = self.posicionx
        self.rect.bottom = self.posiciony

    # Metodo base para realizar el movimiento: simplemente se le indica cual va a hacer, y lo almacena
    def mover(self, movimiento):
        if movimiento == ARRIBA:
            # Si estamos en el aire y el personaje quiere saltar, ignoramos este movimiento
            if self.numPostura == SPRITE_SALTANDO:
                self.movimiento = QUIETO
            else:
                self.movimiento = ARRIBA
        else:
            self.movimiento = movimiento


    def actualizarPostura(self):
        self.retardoMovimiento -= 1
        # Miramos si ha pasado el retardo para dibujar una nueva postura
        if (self.retardoMovimiento < 0):
            self.retardoMovimiento = self.retardoAnimacion
            # Si ha pasado, actualizamos la postura
            self.numImagenPostura += 1
            if self.numImagenPostura >= len(self.coordenadasHoja[self.numPostura]):
                self.numImagenPostura = 0;
            if self.numImagenPostura < 0:
                self.numImagenPostura = len(self.coordenadasHoja[self.numPostura])-1
            self.image = self.hoja.subsurface(self.coordenadasHoja[self.numPostura][self.numImagenPostura])

            # Si esta mirando a la izquiera, cogemos la porcion de la hoja
            if self.mirando == IZQUIERDA:
                self.image = self.hoja.subsurface(self.coordenadasHoja[self.numPostura][self.numImagenPostura])
            #  Si no, si mira a la derecha, invertimos esa imagen
            elif self.mirando == DERECHA:
                self.image = pygame.transform.flip(self.hoja.subsurface(self.coordenadasHoja[self.numPostura][self.numImagenPostura]), 1, 0)



    def movimientoHorizontal(self, incrementox, grupoPlataformas):
        # Esta mirando hacia ese lado
        self.mirando = self.movimiento
        # Actualizamos la posicion
        self.posicionx += incrementox
        self.rect.left = self.posicionx
        # Si no estamos en el aire
        if self.numPostura != SPRITE_SALTANDO:
            # La postura actual sera estar caminando
            self.numPostura = SPRITE_ANDANDO
            # Ademas, si no estamos encima de ninguna plataforma, caeremos
            if pygame.sprite.spritecollideany(self, grupoPlataformas) == None:
                self.numPostura = SPRITE_SALTANDO


    def update(self, grupoPlataformas, tiempo):
        # Si vamos a la izquierda
        if self.movimiento == IZQUIERDA:
            # Realizamos ese movimiento a la izquierda
            self.movimientoHorizontal(-self.velocidad*tiempo, grupoPlataformas)
                
        # Si vamos a la derecha
        elif self.movimiento == DERECHA:
            # Realizamos ese movimiento a la derecha
            self.movimientoHorizontal( self.velocidad*tiempo, grupoPlataformas)

        # Si estamos saltando
        elif self.movimiento == ARRIBA:
            # La postura actual sera estar saltando
            self.numPostura = SPRITE_SALTANDO
            # Le imprimimos una velocidad en el eje y
            self.velocidady = self.velocidadSalto

        # Si no se ha pulsado ninguna tecla
        elif self.movimiento == QUIETO:
            # Si no estamos saltando, la postura actual será estar quieto
            if not self.numPostura == SPRITE_SALTANDO:
                self.numPostura = SPRITE_QUIETO

        # Si estamos en el aire
        if self.numPostura == SPRITE_SALTANDO:
            # Actualizamos la posicion
            self.posiciony -= self.velocidady * tiempo
            # Nos ponemos en esa posicion en el eje y
            self.rect.bottom = self.posiciony

            # Miramos a ver si hay que parar de caer: si hemos llegado a una plataforma
            #  Para ello, miramos si hay colision con alguna plataforma del grupo
            plataforma = pygame.sprite.spritecollideany(self, grupoPlataformas)
            #  Ademas, esa colision solo nos interesa cuando estamos cayendo
            #  y solo es efectiva cuando caemos encima, no de lado, es decir,
            #  cuando nuestra posicion inferior esta por encima de la parte de abajo de la plataforma
            if (plataforma != None) and (self.velocidady<0) and (plataforma.rect.bottom>self.rect.bottom):
                # Lo situamos con la parte de abajo un pixel colisionando con la plataforma
                #  para poder detectar cuando se cae de ella
                self.posiciony = plataforma.rect.top + 1
                self.numPostura = SPRITE_QUIETO
                self.velocidady = 0
                # Nos ponemos en esa posicion en el eje y
                self.rect.bottom = self.posiciony

            # Si no caemos en una plataforma, aplicamos el efecto de la gravedad
            else:
                self.velocidady -= 0.004

        # Actualizamos la imagen a mostrar
        self.actualizarPostura()
        return



# -------------------------------------------------
# Clase Jugador

class Jugador(Personaje):
    "Cualquier personaje del juego"
    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Personaje.__init__(self,'Jugador.png','coordJugador.txt', [6, 12, 6], VELOCIDAD_JUGADOR, VELOCIDAD_SALTO_JUGADOR, RETARDO_ANIMACION_JUGADOR);


    def mover(self, teclasPulsadas, arriba, abajo, izquierda, derecha):
        # Indicamos la acción a realizar segun la tecla pulsada para el jugador
        if teclasPulsadas[arriba]:
            Personaje.mover(self,ARRIBA)
        elif teclasPulsadas[izquierda]:
            Personaje.mover(self,IZQUIERDA)
        elif teclasPulsadas[derecha]:
            Personaje.mover(self,DERECHA)
        else:
            Personaje.mover(self,QUIETO)


# -------------------------------------------------
# Clase NoJugador

class NoJugador(Personaje):
    "El resto de personajes no jugadores"
    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidad, velocidadSalto, retardoAnimacion):
        # Primero invocamos al constructor de la clase padre con los parametros pasados
        Personaje.__init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidad, velocidadSalto, retardoAnimacion);

    # Aqui vendria la implementacion de la IA segun las posiciones de los jugadores
    # La implementacion por defecto, este metodo deberia de ser implementado en las clases inferiores
    #  mostrando la personalidad de cada enemigo
    def mover_cpu(self, jugador1, jugador2):
        # Por defecto un enemigo no hace nada
        #  (se podria programar, por ejemplo, que disparase al jugador por defecto)
        return

# -------------------------------------------------
# Clase Sniper

class Sniper(NoJugador):
    "El enemigo 'Sniper'"
    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        NoJugador.__init__(self,'Sniper.png','coordSniper.txt', [5, 10, 6], VELOCIDAD_SNIPER, VELOCIDAD_SALTO_SNIPER, RETARDO_ANIMACION_SNIPER);

    # Aqui vendria la implementacion de la IA segun las posiciones de los jugadores
    # La implementacion de la inteligencia segun este personaje particular
    def mover_cpu(self, jugador1, jugador2):

        # Movemos solo a los enemigos que esten en la pantalla
        if self.posicionx>0 and self.posicionx<ANCHO_PANTALLA and self.posiciony>0 and self.posiciony<ALTO_PANTALLA:

            # Por ejemplo, intentara acercarse al jugador mas cercano en el eje x
            # Miramos cual es el jugador mas cercano
            if abs(jugador1.posicionx-self.posicionx)<abs(jugador2.posicionx-self.posicionx):
                jugadorMasCercano = jugador1
            else:
                jugadorMasCercano = jugador2
            # Y nos movemos andando hacia el
            if jugadorMasCercano.posicionx<self.posicionx:
                Personaje.mover(self,IZQUIERDA)
            else:
                Personaje.mover(self,DERECHA)

        # Si este personaje no esta en pantalla, no hara nada
        else:
            Personaje.mover(self,QUIETO)

