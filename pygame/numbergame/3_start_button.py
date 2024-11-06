import pygame
# show the start display
def display_start_screen():
     pygame.draw.circle(screen,WHITE,start_button.center,60,5)
     # circle which draw white color and point center is samw as start_botton,
     # radious 60 , line 50
# display game st
def display_game_screen():
     print("game start")
# check pos buttons
def check_buttons(pos):
     global start # 전역변수 global variable
     if start_button.collidepoint(pos):
          start=True
         
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

# game start or not

start =False

# game loop
running = True # going on Game?
while running:
     click_pos =None
     # event loop
     for event in pygame.event.get(): # event?
          if event.type == pygame.QUIT: # Is the event that close window?
               running = False # game over
          elif event.type == pygame.MOUSEBUTTONDOWN: #when user click mouse
               click_pos=pygame.mouse.get_pos()
               print(click_pos)
     # screen color : block
     screen.fill(BLOCK)
     
     if start: # display game screen
          display_game_screen()
     else: # start display
          display_start_screen()
     # update display
     pygame.display.update()
     # if it has value of position which user click
     if click_pos:
          check_buttons(click_pos) 
# game end
pygame.quit

