import serial
import time

# 시리얼 포트 설정 (Windows의 경우 'COM3' 등으로 변경해주세요)
ser = serial.Serial('/dev/cu.usbserial-14230', 9600)  # Linux/Mac 사용자
# ser = serial.Serial('COM3', 9600)  # Windows 사용자

# 아두이노가 준비될 때까지 잠시 대기
time.sleep(2)

try:
    # 1부터 100까지 숫자 전송
    for number in range(1, 101):
        # 숫자를 문자열로 변환하고 개행문자 추가
        data = str(number) + '\n'
        # 문자열을 바이트로 인코딩하여 전송
        ser.write(data.encode())
        # 아두이노의 응답 읽기
        response = ser.readline().decode().strip()
        print(f"Sending Number: {number}, Receiveing : {response}")
        # 잠시 대기
        time.sleep(0.1)

except KeyboardInterrupt:
    print("프로그램을 종료합니다.")

finally:
    # 시리얼 포트 닫기
    ser.close()

