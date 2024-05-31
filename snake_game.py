import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройки змейки
snake_size = 20
snake_speed = 15

# Настройки еды
food_size = 20

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_size, snake_size])

def draw_food(x, y):
    pygame.draw.rect(screen, RED, [x, y, food_size, food_size])

def show_score(score):
    value = font.render(f"Score: {score}", True, BLACK)
    screen.blit(value, [0, 0])

def game_loop():
    game_over = False
    game_close = False

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - food_size) / 20.0) * 20.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - food_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(WHITE)
            message = font.render("Game Over! Press C-Continue or Q-Quit", True, RED)
            screen.blit(message, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(WHITE)
        draw_food(foodx, foody)
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - food_size) / 20.0) * 20.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - food_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
