# Example file showing a basic pygame "game loop"
import sys
import pygame
import map

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bg_image = pygame.image.load("C:\Users\FótiDávidBálint(SZF_\Documents\verseny\images\elefant_sovany.png")
running = True
map = ["coalmine","entrance","kebab","chinese","baguette","british","american","mexican","gym","kuria"]

#flip = update screen pygame.display.flip()
#
while running:
    for event in pygame.event.get(): # poll for 
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0, 0))
    screen.fill("black")
    pygame.display.flip()
    clock.tick(30)

pygame.quit()