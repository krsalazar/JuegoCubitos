import pygame
import sys
import random

ancho = 600
alto = 480
tamano = (ancho, alto)

pygame.init()

pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption('Cubitos')
colorN1 = (26, 184, 78)
colorN2 = (26, 78, 184)
colorN3 = (184, 47, 26)
fondo = (18,89,89)
fuente = pygame.font.Font(None, 30)
colfuente = (0,0,0)
coordenada1 = []
coordenada2 = []
coordenada3 = []
fps = 15
puntos = 0
vidas = 3
nivel = 1
jugando = True
clock = pygame.time.Clock()

for x in range(11):
    x = random.randint(0, ancho - 20)
    y = random.randint(0, 100)
    coordenada1.append([x, y, 20, 20])

for x in range(11):
    x = random.randint(0, ancho - 20)
    y = random.randint(0, 100)
    coordenada2.append([x, y, 20, 20])

for x in range(11):
    x = random.randint(0, ancho - 20)
    y = random.randint(0, 100)
    coordenada3.append([x, y, 20, 20])


while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            i, j = evento.pos

            if nivel == 1:
                for cor in coordenada1:
                    if pygame.draw.rect(pantalla,colorN1, cor).collidepoint(i,j):
                        coordenada1.remove(cor)
                        puntos += 50
            if nivel == 2:
                for cor in coordenada2:
                    if pygame.draw.rect(pantalla,colorN2, cor).collidepoint(i,j):
                        coordenada2.remove(cor)
                        puntos += 50
            if nivel == 3:
                for cor in coordenada3:
                    if pygame.draw.rect(pantalla,colorN3, cor).collidepoint(i,j):
                        coordenada3.remove(cor)
                        puntos += 50
                        
    if len(coordenada1) == 0 and nivel == 1:
        nivel += 1
        fps += 10

    if len(coordenada2) == 0 and nivel == 2:
        nivel += 1
        fps += 10        
    
    pantalla.fill(fondo)
    pantalla_tam = pantalla.get_rect()
    info = fuente.render('Vidas: ' + str(vidas) + ' Puntos: ' + str(puntos).zfill(6) + ' Nivel: ' + str(nivel), True, colfuente)
    tamInfo = info.get_rect()
    tamInfo.topleft = [0,0]
    pantalla.blit(info, tamInfo)

    if vidas > 0:
        if nivel == 1:
            for x in coordenada1:
                pygame.draw.rect(pantalla, colorN1, x)
                x[1] += 1
                if x[1] > alto:
                    x[1] = 0
                    vidas -= 1
                    puntos -= 25
        if nivel ==2:
            for x in coordenada2:
                pygame.draw.rect(pantalla, colorN2, x)
                x[1] += 1
                if x[1] > alto:
                    x[1] = 0
                    vidas -= 1
                    puntos -= 25
        if nivel == 3:
            for x in coordenada3:
                pygame.draw.rect(pantalla, colorN3, x)
                x[1] += 1
                if x[1] > alto:
                    x[1] = 0
                    vidas -= 1
                    puntos -= 25
    else:
        over = fuente.render('Fin del Juego', True, colfuente)
        over_rect = over.get_rect()
        over_rect.center = pantalla_tam.center
        pantalla.blit(over, over_rect)

    pygame.display.flip()
    clock.tick(fps)
sys.exit()