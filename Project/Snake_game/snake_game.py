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

def show_score(choice, color, font, size):
    s_font = pygame.font.SysFont(font, size)
    s_surface = s_font.render("SCORE : ", str(score), True, color)
    s_rect = s_surface.get_rect()
    window.blit(s_surface, s_rect)

def game_over():
    font = pygame.font.SysFont("Roboto", 50)
    go_surface = font.render("Your score is ", str(score), True, blue)
    go_rect = go_surface.get_rect()
    go_rect.midtop = (window_x / 2, window_y / 4)
    window.blit(go_surface, go_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

    quit()