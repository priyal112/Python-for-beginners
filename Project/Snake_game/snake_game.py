import pygame
import time
import random

speed = 13

window_x = 720
window_y = 480

#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

pygame.init()

pygame.display.set_caption("Snake Game")
window = pygame.display.set_mode((window_x, window_y))

snake_position = [100, 60]
snake_body = [[100, 60], [90, 60], [80, 60], [70, 60]]


# generate random food position
def generate_random_food_position():
    return [
        random.randrange(1, (window_x // 10 * 10)),
        random.randrange(1, (window_y // 10 * 10))
    ]

food_positon = generate_random_food_position()

direction = 'RIGHT'

score = 0

