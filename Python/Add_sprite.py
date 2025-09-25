import pygame
import random


spcolorch=pygame.USEREVENT+1
bgcolorch=pygame.USEREVENT+2

blue=pygame.Color('blue')
green=pygame.Color('green')
red=pygame.Color('red')

magenta=pygame.Color('magenta')
yellow=pygame.Color('yellow')
pink=pygame.Color('pink')


class sprite(pygame.sprite.Sprite):
   def __init__(self,color,width,height):
      super().__init__()
      self.image=pygame.Surface([width,height])
      self.image.fill(color)
      self.rect=self.image.get_rect()
      self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
      self.image1=pygame.Surface([width,height])
      self.image1.fill(color)
      self.rect1=self.image.get_rect()
      self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    
   def update(self):
      self.rect.move_ip(self.velocity)
      self.rect1.move_ip(self.velocity)
      boundary=False
      if self.rect.left<=0 or self.rect.right>=500:
         self.velocity[0]=-self.velocity[0]
         boundary=False
      if self.rect.top<=0 or self.rect.bottom>=400:
         self.velocity[1]=-self.velocity[1]
         boundary=False
      if boundary:
         pygame.event.post(pygame.event.Event(spcolorch))
         pygame.event.post(pygame.event.Event(spcolorch))
      if self.rect1.left<=0 or self.rect1.right>=500:
         self.velocity[0]=-self.velocity[0]
         boundary=False
      if self.rect1.top<=0 or self.rect1.bottom>=400:
         self.velocity[1]=-self.velocity[1]
         boundary=False
      if boundary:
         pygame.event.post(pygame.event.Event(spcolorch))
         pygame.event.post(pygame.event.Event(spcolorch))
   def changecolor(self):
      self.image.fill(random.choice([magenta,yellow,pink]))
      self.image1.fill(random.choice([magenta,yellow,pink]))
def changebgcolor(self):
   global bgcolor
   bgcolor=random.choice([blue,green,red])

all_sp=pygame.sprite.Group()
sp=sprite(red,20,30)
sp.rect.x=random.randint(0,480)
sp.rect.y=random.randint(0,370)
all_sp.add(sp)

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Sprites")

bgcolor=blue
screen.fill(bgcolor)
clock=pygame.time.Clock()
exit=False
while not exit:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        exit=True
    elif event.type==spcolorch:
       sp.changecolor()
    elif event.type==bgcolorch:
       changebgcolor()

  all_sp.update()
  screen.fill(bgcolor)
  all_sp.draw(screen)
  pygame.display.flip()
  clock.tick(30)
pygame.quit()