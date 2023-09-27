#SVar is short for Slider Variables
import pygame
import random

#Window Setup
WIDTH =800
HEIGHT = 500
Back_color = (0,0,100)

# Player Setup
GREEN = (0,255,0)
player_size=30
player_pos= [WIDTH/2-player_size/2,HEIGHT-3*player_size]

# Enemy Setup
RED=(255,0,0)
enemy_size=10
enemy_pos= [random.randint(0, WIDTH-enemy_size),0]

#Score
YELLOW=(255,255,0)
score=0

#Font setup
pygame.init()
myFont = pygame.font.SysFont ("monospace",25)

#Setup screen
screen= pygame.display.set_mode((WIDTH,HEIGHT))