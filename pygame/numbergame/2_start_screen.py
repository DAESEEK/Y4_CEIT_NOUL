import pygame
# show the start display
def display_start_screen():
     pygame.draw.circle(screen,WHITE,start_button.center,60,5)
     # circle which draw white color and point center is samw as start_botton,
     # radious 60 , line 50
     
# initial
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Memory Game")
# start button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height -120) # x 는 120 , y 는 전체 높이에서 120을 뺸것
# screen color
BLOCK =(0,0,0) #RGB
WHITE = (255,255,255)

# game loop
running = True # going on Game?
while running:
     # event loop
     for event in pygame.event.get(): # event?
          if event.type == pygame.QUIT: # Is the event that close window?
               running = False # game over
     # screen color : block
     screen.fill(BLOCK)
     # start display
     display_start_screen()
     # update display
     pygame.display.update()
# game end
pygame.quit