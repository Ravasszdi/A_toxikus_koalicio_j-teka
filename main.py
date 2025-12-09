# Example file showing a basic pygame "game loop"
import sys
import pygame
import gombok

# pygame setup
pygame.init()
width = 1920
height = 1080
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
bg_image = pygame.image.load("images/backgrounds/coalmine.png")
running = True
map_ = ["coalmine","entrance","kebab","chinese","baguette","british","american","mexican","gym","kuria"]
font = pygame.font.SysFont('Arial', 36)
map_index = 0

def select(event):
    global map_index
    match event:
        case "bal":
            if gombok.left(map_index) == 2:
                map_index -= 1              
        case "jobb":
            map_index += gombok.right(map_index)
        case _:
            pass
    print(map_index)

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
gomb1 = Button(560, 900, 400, 100, 'Balra lépés', lambda: select("bal"))
gomb2 = Button(960, 900, 400, 100, 'Jobbra lépés', lambda: select("jobb"))
gomb3 = Button(160, 900, 400, 100, 'Tárgy felvétel', lambda: select(""))
gomb4 = Button(1360, 900, 400, 100, 'Használat', lambda: select(""))
gomb5 = Button(1680, 90, 80, 40, 'taco', lambda: select(""))
objects.append(gomb5)
objects.append(gomb1)
objects.append(gomb2)
objects.append(gomb3)
objects.append(gomb4)
labels = ['csiga', 'kebab', 'cica', 'kutya', 'tea', 'fish', 'burgir']

x = 1680
y = 130
w = 80
h = 40
for label in labels:
    btn = Button(x, y, w, h, label, lambda: select("jobb"))
    objects.append(btn)
    y += h  # minden következő gomb 40-nel lejjebb


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