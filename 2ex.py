import pygame
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_INITIAL_LENGTH = 3
INITIAL_SPEED = 10
FOOD_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
FONT_COLOR = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Initialize clock
clock = pygame.time.Clock()

# Initialize font
font = pygame.font.SysFont(None, 30)

# Function to draw the snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Function to generate food
def generate_food(snake):
    while True:
        food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        # Make sure food doesn't overlap with the snake
        if food_pos not in snake:
            return food_pos

# Function to display text on screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
def main():
    # Initialize snake
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    snake_length = SNAKE_INITIAL_LENGTH

    # Initialize food
    food_pos = generate_food(snake)

    # Game variables
    score = 0
    level = 1
    speed = INITIAL_SPEED

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Move the snake
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        # Check for collisions
        if (head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT or
            head in snake[1:]):
            running = False

        # Check for food
        if head == food_pos:
            score += 1
            snake_length += 1
            food_pos = generate_food(snake)
            if score % 3 == 0:  # Increase level every 3 foods eaten
                level += 1
                speed += 2  # Increase speed when level up

        # Update snake length
        if len(snake) > snake_length:
            snake.pop()

        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Draw food
        pygame.draw.rect(screen, FOOD_COLOR, (food_pos[0] * GRID_SIZE, food_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw snake
        draw_snake(snake)

        # Display score and level
        display_text(f"Score: {score}", FONT_COLOR, 10, 10)
        display_text(f"Level: {level}", FONT_COLOR, 10, 30)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(speed)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()