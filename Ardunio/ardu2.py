from pyfirmata2 import Arduino
import time

# 보드와 연결 (포트명을 올바르게 수정하세요)
board = Arduino('/dev/cu.usbserial-141220')

# 보드 초기화 이후 지연
time.sleep(2)  # 2초 대기

# 디지털 핀 13번에 연결된 LED 제어
pin = 13

try:
    while True:
        # LED 켜기
        board.digital[pin].write(1)
        time.sleep(1)
        # LED 끄기
        board.digital[pin].write(0)
        time.sleep(1)
finally:
    board.exit()  # 보드 연결 종료.