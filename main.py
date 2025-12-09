# Example file showing a basic pygame "game loop"
import sys
import pygame
import map

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bg_image = pygame.image.load('background_image.jpg')
running = True
map = ["szenbanya","bejarat","kebab","kinai","baguette","angol","amerikai","mexiko","gym","kuria"]

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