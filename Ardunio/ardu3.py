import serial
import time

# 아두이노와의 시리얼 포트 연결 설정
ser = serial.Serial('/dev/cu.cu.usbserial-14230', 115200)  # 포트 이름과 보드레이트 설정
time.sleep(2)  # 연결 안정화를 위해 잠시 대기

# LED 켜기
ser.write(b'1')
time.sleep(2)

# LED 끄기
ser.write(b'0')
time.sleep(1)

ser.close()  # 시리얼 포트


