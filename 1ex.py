import pygame

pygame.init()
FPS = 60
clock = pygame.time.Clock()

mode = 'blue'

screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

x1 = 0
x2 = 0
y1 = 0
y2 = 0

w = 100
h = 100
color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (194, 6, 6) 
            elif event.key == pygame.K_g:
                color = (95, 235, 52)
            elif event.key == pygame.K_b:
                color = (58, 52, 235)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1 = event.pos[0]
            y1 = event.pos[1]
            isMouseDown = True
        if event.type == pygame.MOUSEMOTION:
            position = event.pos
            points = points + [position]
            points = points[-256:]
            
    screen.fill((0, 0, 0))
       