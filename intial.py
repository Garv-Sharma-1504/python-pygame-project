import pygame
import sys
import random

#initialsising pgame library
pygame.init()

#screen definition
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height))
font_info = pygame.font.SysFont(None,36)
pygame.display.set_caption("Game_Name")

#fps control
clock = pygame.time.Clock()

#definning functions (i.e enemies and such)
class Player:
    x=Width//2
    y=Height//2
    
    #defines the player
    def __init__ (self,x,y):
        #excluding speed for now
        super().__init__()
        #self.image=pygame.surfavce((50,50))
        #self.image.fill((255,0,0))
        #self.rect = self.image.get_rect()
        #self.rect.center = (x, y)
        #self.rect = pygame.Rect(x,y,50,50)
        #self.speed = speed
        self.x = x
        self.y= y
        self.width = 50
        #self.color(110,110,0)
        self.speed = 5
    

    #defines player movement
    def player_input_decide(self):
        key = pygame.key.get_pressed()
        if key == pygame.K_LEFT and self.rect.left > 0:
            self.rect.x -= self.speed
        if key == pygame.K_RIGHT and self.rect.right < Width:
            self.rect.x += self.speed
        if key == pygame.K_UP and self.rect.top > 0:
            self.rect.x -= self.speed
        if key == pygame.K_DOWN and self.rect.bottom < Height:
            self.rect.x += self.speed

    #defining screen blit(()
#    def draw_player(self,surface):
        
#pygame.draw.rect(surface,(100,100,100),self.rect)

#Creating player and enemies:
#player = Player1(Width//2,Height//60)
Player1 = Player()
#Player1.x= Width//2
#Player1.y=Height//2
player = Player1(Width//2,Height//2)
x=width//2
y= Height//2

#Running loop 
running=True
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update game objects :
    Player1.player_input_decide()
    
    screen.fill((0,0,0))
    running_text= font_info.render("the game is running ........ I suppose",True,(111,120,32))
    screen.blit(running_text,(50,Height//2))

    #player render
    ##player.draw_player(screen)
    pygame.draw.rect(sceen,(100,100,100),player.rect)

    #pygame.display.update()
    pygame.display.flip()

    #fps limiter
    clock.tick(45)
    
pygame.quit()
sys.exit()
