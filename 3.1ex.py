import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the drawing window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Paint Program')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Default brush color
current_color = BLACK

# Brush sizes
brush_size = 5

# Font for displaying text
font = pygame.font.SysFont(None, 24)

# Create a surface to draw on
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_surface.fill(WHITE)

# Run the game loop
running = True
drawing = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
            elif event.button == 3:  # Right mouse button
                drawing_surface.fill(WHITE)  # Clear the drawing surface
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_w:
                current_color = WHITE
            elif event.key == pygame.K_1:
                brush_size = 5
            elif event.key == pygame.K_2:
                brush_size = 10
            elif event.key == pygame.K_3:
                brush_size = 20
            elif event.key == pygame.K_4:
                brush_size = 30

    # Draw on the surface if the mouse button is pressed
    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(drawing_surface, current_color, pos, brush_size)

    # Clear the screen
    window.fill(WHITE)

    # Draw the drawing surface onto the window
    window.blit(drawing_surface, (0, 0))

    # Display instructions
    text = font.render("Press 1, 2, 3, or 4 to change brush size", True, BLACK)
    window.blit(text, (10, 10))
    text = font.render("Press 'r' for red, 'g' for green, 'b' for blue, 'w' for white", True, BLACK)
    window.blit(text, (10, 30))
    text = font.render("Left click to draw, right click to clear", True, BLACK)
    window.blit(text, (10, 50))

    # Update the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()