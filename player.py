import pygame
import SVar
import sys
import time

def drawplayer():
  clicked=False
  button=pygame.Rect(0,SVar.HEIGHT-50,100,50)
  pygame.draw.rect(SVar.screen,(255,255,255),button)
  mousePos=pygame.mouse.get_pos()
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.MOUSEBUTTONUP:
      clicked=True
      x=SVar.player_pos[0]
      y= SVar.player_pos[1]
      mousePos=pygame.mouse.get_pos()
      if button.collidepoint(mousePos):
        SVar.player_pos[0]-=SVar.player_size
        print("left")
        
        

    

    if event.type == pygame.KEYDOWN:
   
      x=SVar.player_pos[0]
      y= SVar.player_pos[1]

      

      if event.key == pygame.K_LEFT:
        x -= SVar.player_size

      if event.key == pygame.K_RIGHT:
        x += SVar.player_size
      
      SVar.player_pos=[x,y]
  
  pygame.draw.rect(SVar.screen,SVar.GREEN,(SVar.player_pos[0],SVar.player_pos[1],SVar.player_size,SVar.player_size))

# Suppose we have a variable "grade" representing a student's grade in a test
grade = 85

# Let's use "if" and "elif" statements to classify the student's performance
if grade >= 90:
    print("Excellent! You got an A.")
elif grade >= 80:
    print("Good job! You got a B.")
elif grade >= 70:
    print("Keep it up! You got a C.")
else:
    print("You need to work harder. Your grade is below C.")

