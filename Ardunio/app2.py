# 아두이노 LED 세개를 web 화면에 조작하고 기록하는 프로 그램입니다 
# Arduino와 이프로그램임은 프레인 뭐크 기능을 위해하고 template 
#데이타 베이스는 post
# 이릉위해서 brew start postgresql을 시켜야 합니다. 

from flask import Flask, render_template, request, jsonify
import serial
import time
import psycopg2
from datetime import datetime
import pytz

app = Flask(__name__)

arduino = serial.Serial('/dev/cu.usbserial-DJ00H5Q2', 9600) 
# 아두이노와의 시리얼 포트 연결 설정
#arduino = serial.Serial('/dev/cu.usbserial-14230', 9600)  # 실제 포트로 변경
time.sleep(2)  # 시리얼 연결 안정화 대기

# PostgreSQL 데이터베이스 연결 설정
conn = psycopg2.connect(
    dbname="postgres",  # 기본 데이터베이스인 'postgres' 사용
    user="daeseekpaek",
    password="",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
# 한국 표준시로 변환하는 함수
def get_local_time(utc_time):
    kst = pytz.timezone('Asia/Vientiane')
    return utc_time.astimezone(kst).strftime('%Y-%m-%d %H:%M:%S')

# 테이블이 없으면 생성하는 함수
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS led_log (
            id SERIAL PRIMARY KEY,
            color VARCHAR(10) NOT NULL,
            action VARCHAR(4) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

# 테이블이 없을 경우 생성
create_table()

# LED 점등 기록을 데이터베이스에 저장하는 함수
def log_led_action(color, action):
    cursor.execute(
        "INSERT INTO led_log (color, action) VALUES (%s, %s)",
        (color, action)
    )
    conn.commit()

@app.route('/')
def index():
    try:
        return render_template('index2.html')
    except Exception as e:
        print(f"템플릿 렌더링 오류: {str(e)}")  # 오류 내용 출력
        return str(e), 500  # 오류 메시지를 브라우저에 표시

@app.route('/led', methods=['POST'])
def led():
    color = request.form['color']
    action = request.form['action']
    command = f"{color.upper()}_{action.upper()}"
    arduino.write(command.encode())  # 명령 전송
    log_led_action(color, action)  # 데이터베이스에 로그 기록
    return 'OK'

# LED 점등 기록 조회 API
@app.route('/led_log', methods=['GET'])
def led_log():
    cursor.execute("SELECT color, action, timestamp FROM led_log ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)