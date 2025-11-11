import pygame
import sys

#initialsising pgame library
pygame.init()

#screen definition
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height))
font_info = pygame.font.SysFont(None,36)

#definning functions


#Running loop 
running=True
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    running_text= font_info.render("the game is running ........ I suppose",True,(111,120,32))
    screen.blit(running_text,(50,Height//2))
    #pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()
