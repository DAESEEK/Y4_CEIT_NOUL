import pygame

# initial
pygame.init()
screen_width = 720 # 가로크기
screen_height = 1280 # 세로크기

screen = pygame.display.set_mode((screen_height,screen_width))

pygame.display.set_caption("Memory Game")

# game loop
running = True # going on Game?
while running:
     
     for event in pygame.event.get(): # event?
          if event.type == pygame.QUIT: # Is the event that close window?
               running = False # There is not working game
# end game
pygame.quit()
     