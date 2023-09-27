import pygame
import SVar
import random

def drawenemy():
  if SVar.enemy_pos[1] >=0 and SVar.enemy_pos[1] < SVar.HEIGHT:
    SVar.enemy_pos[1] += 10
  else:
    SVar.enemy_pos[0]= random.randint(0,SVar.WIDTH-SVar.enemy_size)
    SVar.enemy_pos[1]=0
  pygame.draw.rect(SVar.screen,SVar.RED,(SVar.enemy_pos[0],SVar.enemy_pos[1],SVar.enemy_size,SVar.enemy_size))