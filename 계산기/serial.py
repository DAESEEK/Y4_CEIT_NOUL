from arduino import Arduino
import time

# 포트와 보드 연결 설정
b = Arduino('/dev/cu.usbserial-141220')
pin = 4  # 디지털 핀 번호

# 핀 모드 설정 (OUTPUT)
b.pinMode(pin, b.OUTPUT)

print("Control the LED at pin 4.")
print("Enter 1 to turn ON the LED, 2 to turn it OFF, anything else to exit.")

try:
    while True:
        cmd = input("Enter your command: ")
        if cmd == '1':
            b.digitalWrite(pin, b.HIGH)  # LED 켜기
            print("LED is ON.")
        elif cmd == '2':
            b.digitalWrite(pin, b.LOW)  # LED 끄기
            print("LED is OFF.")
        else:
            print("Exiting program.")
            break
finally:
    b.close()  # 포트 닫기 및 자원 해제