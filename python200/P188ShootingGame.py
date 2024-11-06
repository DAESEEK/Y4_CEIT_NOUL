#from time import clock_getres
import pygame
# 게임에 사용되는 전역변수 정의 ຕົວແປທົ່ວໂລກ global variable
BLACK =(0,0,0)
pad_width = 480
pad_height = 640

# 게임에서 사용되는 메인 함수 main function
def runGame():
     global gamepad,clock_getres

     doneFlag = False
     while not doneFlag:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    doneFlag = True
          # 게임화면을 검은 색으로 채우고 화면을 업데이트함 chnage colar to block and update screen
          gamepad.fill(BLACK)
          pygame.display.update()
          clock.tick(60)

     pygame.quit()

# 게임 초기화 함수 initial game function
def initGame():
     global gamepad,clock

     pygame.init()
     gamepad = pygame.display.set_mode((pad_width,pad_height))
     pygame.display.set_caption('MyGalaga')
     clock = pygame.time.Clock()

initGame()
runGame()


               
