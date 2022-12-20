import pygame
import sys

def checkAllKeys ( a , b , c ):
   if a == True and b == True and c == True:
      ev = pygame.event.Event ( pygame.USEREVENT )
      pygame.event.post ( ev )
pygame.display.init()
screen = pygame.display.set_mode ( ( 320 , 240 ) )
pressedA = False
pressedB = False
pressedC = False
while 1:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      elif event.type == pygame.KEYDOWN:
         if event.key == ord ( "a" ): pressedA = True
         elif event.key == ord ( "b" ): pressedB = True
         elif event.key == ord ( "c" ): pressedC = True
         checkAllKeys ( pressedA , pressedB , pressedC )
      elif event.type == pygame.USEREVENT:
         print ( "You have pressed a, b, and c" )