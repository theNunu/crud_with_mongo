import pygame
import sys

pygame.init()
ancho, alto = 500, 300
pantalla = pygame.display.set_mode((ancho, alto))

jugador = pygame.Rect(50, 50, 20, 20)
velocidad = 20

while True:
    pantalla.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: jugador.x -= velocidad
    if keys[pygame.K_RIGHT]: jugador.x += velocidad
    if keys[pygame.K_UP]: jugador.y -= velocidad
    if keys[pygame.K_DOWN]: jugador.y += velocidad

    pygame.draw.rect(pantalla, (0, 255, 0), jugador)

    pygame.display.flip()
    pygame.time.delay(30)