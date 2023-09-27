import time
import SVar
import pygame

start_time=time.time()
game_time=30

def timer():
  Total_time= time.time()-start_time
  text= "Time: "+str(int(Total_time))

  label =SVar.myFont.render(text,1,SVar.YELLOW)
  SVar.screen.blit(label,(0,0))
  if Total_time> game_time:
    return True
  else:
    return False

def endscreen():
  SVar.screen.fill(SVar.GREEN)
  text='Game Over'
  label = SVar.myFont.render(text,1,SVar.YELLOW)
  SVar.screen.blit(label,(0,SVar.HEIGHT/2))

  text='Score:'+ str(SVar.score)
  label = SVar.myFont.render(text,1,SVar.YELLOW)
  SVar.screen.blit(label,(0,SVar.HEIGHT/2+30))
  pygame.display.update()