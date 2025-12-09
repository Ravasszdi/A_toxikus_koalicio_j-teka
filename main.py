# Example file showing a basic pygame "game loop"
import sys
import pygame
import map

# pygame setup
pygame.init()
width = 1920
height = 1080
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
bg_image = pygame.image.load("images/backgrounds/coalmine.png")
running = True
map = ["coalmine","entrance","kebab","chinese","baguette","british","american","mexican","gym","kuria"]
font = pygame.font.SysFont('Arial', 40)
def myFunction():
    print('Button Pressed')
objects = []
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        screen.blit(self.buttonSurface, self.buttonRect)
gomb1 = Button(560, 880, 400, 100, 'Balra lépés', myFunction)
gomb2 = Button(960, 880, 400, 100, 'Jobbra lépés', myFunction)
objects.append(gomb1)
objects.append(gomb2)
print(gomb1.width)
#flip = update screen pygame.display.flip()
#
while running:
    for event in pygame.event.get(): # poll for 
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0, 0))
    for object in objects:
        object.process()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()