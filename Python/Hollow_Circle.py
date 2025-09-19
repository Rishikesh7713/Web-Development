import pygame
import sys
pygame.init()
window=pygame.display.set_mode((400,400))
window.fill((0,0,0))
green=((0,255,0))
pygame.draw.circle(window,green,(300,300),50)
pygame.draw.circle(window,green,(100,100),50,3)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()        
sys.exit()