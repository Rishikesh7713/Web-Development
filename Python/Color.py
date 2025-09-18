import pygame
pygame.init()
def main():
   sc_w,sc_h=(1000,900)
   screen=pygame.display.set_mode((sc_w,sc_h))
   pygame.display.set_caption("Color changing game")

   color={
     'red':pygame.Color('red'),
     'green':pygame.Color('green'),
     'blue':pygame.Color('blue'),
     'violet':pygame.Color('violet'),
     'white':pygame.Color('white')
   }
   current_color=color['white']
   x,y=30,30
   sw,sh=60,60

   clock=pygame.time.Clock()

   done=False
   while not done:
      for event in pygame.event.get():
         if event.type==pygame.QUIT:
            done=True
      pressed=pygame.key.get_pressed()
      if pressed[pygame.K_LEFT]:x-=3
      if pressed[pygame.K_RIGHT]:x+=3
      if pressed[pygame.K_UP]:y-=3
      if pressed[pygame.K_DOWN]:y+=3

      x=min(max(0,x),sc_w-sw)
      y=min(max(0,y),sc_h-sh)

      if x==0:current_color=color['red']
      elif x==sc_w-sw:current_color=color['blue']
      elif y==0:current_color=color['green']
      elif y==sc_h-sh:current_color=color['violet']
      else:
         current_color=color['white']

      screen.fill((0,0,0))
      pygame.draw.rect(screen,current_color,(x,y,sw,sh))
      pygame.display.flip()
      clock.tick(90)
   pygame.quit()
if __name__=='__main__':
   main()