import SVar
import pygame

def detect_collision(ps,es):
  if (es[0]>=ps[0] and es[0] < (ps[0]+SVar.player_size)) or (es[0]<=ps[0] and es[0]>(ps[0]+SVar.player_size)):
    
    if (es[1]>=ps[1] and es[1] < (ps[1]+SVar.player_size)) or (es[1]<=ps[1] and es[1]>(ps[1]+SVar.player_size)):

      SVar.score +=1

  text='Score:'+ str(SVar.score)
  label = SVar.myFont.render(text,1,SVar.YELLOW)
  SVar.screen.blit(label,(0,SVar.HEIGHT-20))