import pygame
import time
import random


pygame.init()


width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)


block_size = 10
snake_speed = 15


font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def display_score(score):
    value = score_font.render(f"Score: {score}", True, black)
    screen.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block_size, block_size])

def game():
    game_over = False
    game_close = False

    
    x, y = width / 2, height / 2
    x_change, y_change = 0, 0

    
    snake_list = []
    snake_length = 1

    
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            screen.fill(white)
            message = font_style.render("Game Over! Press C-Play Again or Q-Quit", True, red)
            screen.blit(message, [width / 6, height / 3])
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game()
