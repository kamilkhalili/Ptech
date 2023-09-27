import pygame
import SVar
import player
import enemy
import timer
import Collision

game_over=False
clock= pygame.time.Clock()
pygame.init()

while not game_over:
  SVar.screen.fill((SVar.Back_color))
  player.drawplayer()
  enemy.drawenemy()
  Collision.detect_collision(SVar.player_pos,SVar.enemy_pos)
  game_over=timer.timer()
  clock.tick(30)
  
  pygame.display.update()
  
timer.endscreen() 