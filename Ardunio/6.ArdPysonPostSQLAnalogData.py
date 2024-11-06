import serial
import psycopg2
import time
# 아두이노 시리얼 포트 설정 (운영체제에 따라 COM 포트를 맞춤 설정 필요)
arduino = serial.Serial('/dev/cu.usbserial-14230', 9600) 
time.sleep(2)  # 아두이노와의 연결 안정화 대기

# PostgreSQL 연결 설정
conn = psycopg2.connect(
    database="sensor_data",
    user="postgres",
    password=""  # PostgreSQL 비밀번호 입력
)
cursor = conn.cursor()
def save_data_to_postgresql(value):
    # 데이터 저장 SQL 쿼리
    query = "INSERT INTO sensor_values (value) VALUES (%s)"
    cursor.execute(query, (value,))
    conn.commit()
    print(f"Saved to PostgreSQL: {value}")

try:
    while True:
        # 아두이노 데이터 읽기
        if arduino.in_waiting > 0:
            line = arduino.readline().decode().strip()
            if line.isdigit():  # 숫자인지 확인 후 저장
                value = int(line)
                if value > 500:  # LED 켜짐 기준값
                    print("LED ON")
                else:
                    print("LED OFF")
                save_data_to_postgresql(value)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    # 연결 종료
    cursor.close()
    conn.close()
    arduino.close()
