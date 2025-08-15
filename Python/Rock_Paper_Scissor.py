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
    self.p_option="rock"
    self.screen.blit(self.choose_rbtn(120,200))
   elif self.paper_btn.clicked(30):
    self.p_option="paper"
    self.screen.blit(self.choose_pbtn(120,200))
   else:
    self.p_option="scissor"
    self.screen.blit(self.choose_sbtn(120,200))

    return self.p_option()
   
  def computer(self):
   self.pc_random_choice=" "
   option=["rock","paper","scissor"]
   pcchoice=random.choice(list(option))
   if pcchoice=="rock":
    self.pc_random_choice="rock"
    pcchoice=self.choose_rbtn
   elif pcchoice=="paper":
    self.pc_random_choice="paper"
    pcchoice=self.choose_pbtn
   else:
    self.pc_random_choice="scissor"
    pcchoice=self.choose_sbtn
   pc_option=self.screen.blit(pcchoice,(600,200))
   return pc_option()
  
  def pl_score_cache(self):
   self.pl_score=0
   self.pc_score=0
   pl=self.p_option
   pc=self.pc_random_choice
   if pl=="rock"and pc=="paper" or pl=="paper"and pc=="scissor" or pl=="scissor"and pc=="rock":
    self.pc_score+=1
   elif pc==pl:
    pass
   else:
    self.pl_score+=1
   return self.pl_score()
  
  def pc_score_cache(self):
   self.pl_score=0
   self.pc_score=0
   pl=self.p_option
   pc=self.pc_random_choice
   if pc=="rock"and pl=="paper" or pc=="paper"and pl=="scissor" or pc=="scissor"and pl=="rock":
    self.pl_score+=1
   elif pc==pl:
    pass
   else:
    self.pc_score+=1
   return self.pc_score()
  
  def image_reset(self):
   self.screen.blit(self.text,(330,0))
   self.text=self.font.render("",True,(0,0,0))
   self.screen.blit(self.rbtn,(20,500))
   self.screen.blit(self.pbtn,(330,500))
   self.screen.blit(self.sbtn,(640,500))
   pass
  
 def game_loop(self):
   run=True
   clock=pygame.time.Clock
   Rps_game=Rpsgame()
   while run:
    pygame.display.update()
    self.screen.blit(self.text,(330,0))
    for event in pygame.event.get():
     if event.type==pygame.quit:
      run=False
     if event.type==pygame.MOUSEBUTTONDOWN:
      if self.rock_btn.clicked(30) or self.paper_btn.clicked(340) or self.scissor_btn.clicked(640):
       Rps_game.image_reset()
       Rps_game.player()
       Rps_game.computer()
       self.pl_score()+=Rps_game.pl_score_cache()
       self.pc_score()+=Rps_game.pc_score_cache()
       self.text=self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255,255,255))
    pygame.display.flip()
    clock.tick(30)
   pygame.quit()

 if __name__=='__main__':
   game=Rpsgame()
   game.game_loop 

    

   