# Example file showing a basic pygame "game loop"
import sys
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
#flip = update screen pygame.display.flip()
#
while running:
    for event in pygame.event.get(): # poll for 
        
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.display.flip()
    clock.tick(30)

pygame.quit()