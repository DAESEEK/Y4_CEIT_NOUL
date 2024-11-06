import serial
import time

# 시리얼 포트 연결 (Mac OS)
ser = serial.Serial('/dev/cu.usbserial-14230', 9600, timeout=1)
time.sleep(2)  # 아두이노 리셋을 위한 대기 시간

try:
    while True:
        # 사용자로부터 두 수 입력받기
        num1 = input("첫 번째 숫자를 입력하세요: ")
        num2 = input("두 번째 숫자를 입력하세요: ")
        
        # 아두이노로 데이터 전송
        ser.write(f"{num1}\n{num2}\n".encode())
        
        # 아두이노로부터 결과 받기
        result = ser.readline().decode().strip()
        
        print(f"결과: {result}")
        
        # 계속할지 물어보기
        continue_calc = input("계속하시겠습니까? (y/n): ")
        if continue_calc.lower() != 'y':
            break

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
finally:
    ser.close()  # 시리얼 포트 닫기
