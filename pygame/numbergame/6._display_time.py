from random import *
import pygame

# level setting
def setup(level):
     # how long show the number?
     global display_time
     display_time = 5-(level//3)
     display_time = max(display_time,1) # 1 sec 
     # how many display numbers?
     number_count = (level//3)+5
     number_count = min(number_count,20) # 20 
     # display random number on the screen 
     shuffle_grid(number_count)
# number mixed (important point in this program)
def shuffle_grid(number_count):
     rows=5
     columns = 9
     
     cell_size = 130 # grid each cell size(raw col)
     button_size = 110 # button size in Grid cell 
     screen_left_margin = 55 # whole screen left side margn in whole screen 
     screen_top_margin = 20 # 
     
     # [[0,0,0,0,0,0,5,0,0],
     #  [0,0,0,1,0,0,4,0,0],
     #  [0,0,0,0,2,0,0,0,0],
     #  [0,0,3,0,0,0,0,0,0],
     #  [0,0,0,0,0,0,0,0,0]]
     grid = [[0 for col in range(columns)] for row in range(rows)] # 5*9
     
     number = 1 # from 1 until number_count 
     while number <=number_count:
          row_idx = randrange(0,rows) # 0,1,2,3,4
          col_idx = randrange(0,columns) #0,1,2,3,4,5,6,7,8
          
          if grid[row_idx][col_idx]==0:
               grid[row_idx][col_idx] = number # define number
               number +=1
               # grid cell pos x,y 
               center_x=screen_left_margin+(col_idx * cell_size)+(cell_size/2)
               center_y=screen_top_margin +(row_idx*cell_size)+(cell_size/2)
               
               # make number button
               button=pygame.Rect(0,0,button_size,button_size)
               button.center = (center_x,center_y)
               
               number_buttons.append(button)
               
     # check defind numbers
     print(grid)
     
# show the start display
def display_start_screen():
     pygame.draw.circle(screen,WHITE,start_button.center,60,5)
     # circle which draw white color and point center is samw as start_botton,
     # radious 60 , line 50






# display game screen
def display_game_screen():
     global hidden
     
     if not hidden:
          elapased_time =(pygame.time.get_ticks()-start_ticks)/1000 # ms==> sec
          if elapased_time > display_time:
               hidden = True
               
     for idx, rect in enumerate(number_buttons,start=1):
          if hidden : # process hidden
               
          # draw rectangle button   
             pygame.draw.rect(screen,GRAY,rect)
          else:   
          # real number text
               cell_text = game_font.render(str(idx),True,WHITE)
               text_rect = cell_text.get_rect(center=rect.center)
               screen.blit(cell_text,text_rect)
          
# check pos buttons
def check_buttons(pos):
     global start,start_ticks # 전역변수 global variable
     
     if start : # If the game is starting?
          check_number_buttons(pos)
     elif start_button.collidepoint(pos):
          start=True
          start_ticks =pygame.time.get_ticks()

def check_number_buttons(pos):
     global hidden
     
     for button in number_buttons:
          if button.collidepoint(pos):
               if button==number_buttons[0]: # clicked correct number
                    print("correct")
                    del number_buttons[0]
                    if not hidden:
                         hidden= True # hide number
               else: # clicked wrong number
                    print("wrong") 
               break 
# initial
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None,120) # define font

# start button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height -120) # x 는 120 , y 는 전체 높이에서 120을 뺸것
# screen color
BLOCK =(0,0,0) #RGB
WHITE = (255,255,255)
GRAY = (50,50,50)

number_buttons =[] # Buttons that a player has to click 
display_time = None # time for showing numbers
start_tick = None # calcurate time
# game start or not
start =False





# number hide or not (user click 1 or time out)
hidden =False


# before geme start, act def
setup(1)
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