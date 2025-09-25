import pygame
import random 
sw,sh=500,400
speed=5
fonts=75
pygame.init()
bg=pygame.transform.scale(pygame.image.load('download.jpg'),(sw,sh))
font=pygame.font.SysFont("Times New Roman", fonts)

class sprite(pygame.sprite.Sprite):
   def __init__(self,color,width,height):
    super().__init__()
    self.image=pygame.Surface([width,height])
    self.image.fill(pygame.Color('dodgerblue'))
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect()

   def move(self,xchange,ychange):
     self.rect.x=max(min(self.rect.x + xchange, sw-self.rect.width),0)
     self.rect.y=max(min(self.rect.y+ ychange, sh-self.rect.height),0)

screen=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Color changing game")
allsp=pygame.sprite.Group()

sp1=sprite(pygame.Color('black'),20,30)
sp1.rect.x,sp1.rect.y=random.randint(0,sw-sp1.rect.width),random.randint(0,sh-sp1.rect.height)
allsp.add(sp1)
sp2=sprite(pygame.Color('red'),20,30)
sp2.rect.x,sp2.rect.y=random.randint(0,sw-sp2.rect.width),random.randint(0,sh-sp2.rect.height)
allsp.add(sp2)

running,won=True,False
clock=pygame.time.Clock()
while running:
  for event in pygame.event.get():
    if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_x:
      running=False

  if not won:
    keys=pygame.key.get_pressed()
    xchange=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*speed
    ychange=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*speed
    sp1.move(xchange,ychange)

    if sp1.rect.colliderect(sp2.rect):
      allsp.remove()
      won=True
  screen.blit(bg,(0,0))
  allsp.draw(screen)
  if won:
    wintext=font.render("You Win!",True,pygame.Color('black'))
    screen.blit(wintext,((sw-wintext.get_width())//2,(sh-wintext.get_height())//2))

  pygame.display.flip()
  clock.tick(90)
pygame.quit()