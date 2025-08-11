import random
import pygame
class button():
 def _init_(self, x, y, pos, width, height):
  self.x=x
  self.y=y
  self.pos=pos
  self.width=width
  self.height=height
 class Rpsgame():
  def _init_(self):
   pygame.init()

   self.screen=pygame.display.set_mode((960,640))
   pygame.display.set_caption("RPS Display")

   self.bg=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\background.jpg")
   self.rbtn=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\r_button.png").convert_alpha()
   self.pbtn=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\p_button.png").convert_alpha()
   self.sbtn=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\s_button.png").convert_alpha()
   self.choose_rbtn=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\pc_rock.png").convert_alpha()
   self.choose_pbtn=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\pc_paper.png").convert_alpha()
   self.choose_sbtn=pygame.image.load("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\pc_scissors.png").convert_alpha()

   self.screen.blit(self.bg,(0,0))
   self.screen.blit(self.rbtn,(20,500))
   self.screen.blit(self.bg,(330,500))
   self.screen.blit(self.bg,(640,500))

   self.rock_btn= Button(30,520(30,520),30,140)
   self.paper_btn= Button(340,520(340,520),30,140)
   self.scissor_btn= Button(640,520(640,520),30,140)

   self.font=pygame.font.Font(("C:\Users\ponnu\OneDrive\画像\Codingal stuff\Web Development\Web-Development\Python\Splatch.ttf"),90)
   self.text=self.font.render(f" ",True,255,255,255)

   self.pl.score=0
   self.pc.score=0

  def player(self):
   if self.rock_btn.clicked(30):
    self.option="rock"
    self.screen.blit(self.choose_rbtn(120,200))
   elif self.paper_btn.clicked(30):
    self.option="paper"
    self.screen.blit(self.choose_pbtn(120,200))
   else:
    self.option="scissor"
    self.screen.blit(self.choose_sbtn(120,200))

    return self.option()
   
