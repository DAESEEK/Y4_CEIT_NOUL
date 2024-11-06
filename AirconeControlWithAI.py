from flask import Flask, request, jsonify, render_template
import requests
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

app = Flask(__name__)

# PostgreSQL 설정
conn = psycopg2.connect(
    host="localhost",
    database="weather_db",
    user="postgres",
    password=""
)

# 테이블 생성
def create_table():
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id SERIAL PRIMARY KEY,
                temperature FLOAT NOT NULL,
                humidity FLOAT NOT NULL,
                discomfort_index FLOAT NOT NULL,
                ac_status VARCHAR(3) DEFAULT 'OFF',
                timestamp TIMESTAMP NOT NULL
            )
        """)
        conn.commit()

# OpenWeatherMap API 설정
OPENWEATHERMAP_API_KEY = 'f761d06ee6470da39cb6d1070febf362'
LOCATION = 'Vientiane,LA'

# 초기 에어컨 상태 및 자동 제어 조건 설정
ac_status = "OFF"
on_conditions = [(28, 60), (30, 50)]  # ON 조건
off_conditions = [(24, 40), (23, 50)] # OFF 조건

# 불쾌지수 계산 함수
def calculate_discomfort_index(temp, humidity):
    return round(0.81 * temp + 0.01 * humidity * (0.99 * temp - 14.3) + 46.3, 2)

# 온습도 데이터를 OpenWeatherMap에서 가져와 PostgreSQL에 저장
def update_weather_data():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"API 호출 실패. 상태 코드: {response.status_code}")
            print(f"에러 메시지: {response.text}")
            return
            
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        discomfort_index = calculate_discomfort_index(temperature, humidity)
        
        # 디버깅 출력 추가
        print(f"API 응답: {data}")
        print(f"현재 온도: {temperature}°C")
        print(f"현재 습도: {humidity}%")
        print(f"불쾌지수: {discomfort_index}")
        
        # 데이터베이스에 저장
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO weather_data (temperature, humidity, discomfort_index, timestamp) 
                VALUES (%s, %s, %s, %s)
            """, (temperature, humidity, discomfort_index, datetime.now()))
            conn.commit()
        print(f"날씨 업데이트 완료: 온도={temperature}°C, 습도={humidity}%, 불쾌지수={discomfort_index}")
    except Exception as e:
        print(f"날씨 데이터 업데이트 중 오류 발생: {str(e)}")

class ACController:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.initial_conditions = True  # 초기에는 기본 조건 사용
        self.min_training_samples = 100  # 학습에 필요한 최소 데이터 수
        
    def get_training_data(self):
        """데이터베이스에서 학습 데이터 가져오기"""
        with conn.cursor() as cur:
            cur.execute("""
                SELECT temperature, humidity, discomfort_index, ac_status 
                FROM weather_data 
                WHERE timestamp >= NOW() - INTERVAL '7 days'
            """)
            data = cur.fetchall()
            return pd.DataFrame(data, columns=['temperature', 'humidity', 'discomfort_index', 'ac_status'])
    
    def train_model(self):
        """모델 학습"""
        data = self.get_training_data()
        if len(data) < self.min_training_samples:
            return False
        
        X = data[['temperature', 'humidity', 'discomfort_index']]
        y = (data['ac_status'] == 'ON').astype(int)
        
        self.model.fit(X, y)
        self.initial_conditions = False  # 학습 후에는 기본 조건 사용 안 함
        return True
    
    def determine_ac_status(self, temperature, humidity, discomfort_index):
        """에어컨 상태 결정"""
        if self.initial_conditions:
            # 초기 기본 조건 사용
            for temp_cond, humid_cond in on_conditions:
                if temperature >= temp_cond and humidity >= humid_cond:
                    return "ON"
            for temp_cond, humid_cond in off_conditions:
                if temperature <= temp_cond and humidity <= humid_cond:
                    return "OFF"
            return ac_status  # 현재 상태 유지
        else:
            # 학습된 모델 사용
            prediction = self.model.predict([[temperature, humidity, discomfort_index]])
            return "ON" if prediction[0] == 1 else "OFF"

# 컨트롤러 인스턴스 생성
ac_controller = ACController()

# 24시간 에어컨 동작 시간 계산
def calculate_ac_runtime():
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*) FROM weather_data 
        WHERE timestamp >= %s AND ac_status = 'ON'
    """, (datetime.now() - timedelta(hours=24),))
    runtime_count = cur.fetchone()[0]
    runtime_hours = runtime_count / (60 / 2)  # 2시간 간격 데이터 기준
    return round(runtime_hours, 2)

@app.route('/set_ac_status', methods=['POST'])
def set_ac_status():
    global ac_status
    data = request.get_json()
    new_status = data.get('status')
    
    if new_status in ['ON', 'OFF']:
        ac_status = new_status
        # 데이터베이스에 상태 업데이트
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE weather_data 
                SET ac_status = %s 
                WHERE id = (SELECT id FROM weather_data ORDER BY timestamp DESC LIMIT 1)
            """, (ac_status,))
            conn.commit()
        return jsonify({'status': ac_status})
    return jsonify({'error': 'Invalid status'}), 400

@app.route('/dashboard', methods=['GET'])
def dashboard():
    cur = conn.cursor()
    cur.execute("SELECT temperature, humidity, discomfort_index, ac_status FROM weather_data ORDER BY timestamp DESC LIMIT 1")
    latest_weather = cur.fetchone()
    
    ac_runtime = calculate_ac_runtime()

    if latest_weather:
        temperature, humidity, discomfort_index, current_ac_status = latest_weather
        return jsonify({
            "temperature": temperature,
            "humidity": humidity,
            "discomfort_index": discomfort_index,
            "ac_runtime_last_24h": ac_runtime,
            "ac_status": current_ac_status  # AC 상태 추가
        })
    else:
        return jsonify({"error": "No data available"}), 404

# 주기적으로 날씨 데이터를 업데이트 및 학습 조건 업데이트
def periodic_updates():
    """주기적 업데이트 및 학습"""
    while True:
        update_weather_data()
        
        # 현재 데이터 가져오기
        with conn.cursor() as cur:
            cur.execute("""
                SELECT temperature, humidity, discomfort_index 
                FROM weather_data 
                ORDER BY timestamp DESC LIMIT 1
            """)
            latest_data = cur.fetchone()
        
        if latest_data:
            temperature, humidity, discomfort_index = latest_data
            
            # 일정 주기로 모델 재학습
            if time.time() % (24 * 3600) < 300:  # 하루에 한 번 학습
                ac_controller.train_model()
            
            # 상태 결정 및 업데이트
            global ac_status
            new_status = ac_controller.determine_ac_status(temperature, humidity, discomfort_index)
            
            if new_status != ac_status:
                ac_status = new_status
                # 데이터베이스에 상태 업데이트 추가
                with conn.cursor() as cur:
                    cur.execute("""
                        UPDATE weather_data 
                        SET ac_status = %s 
                        WHERE id = (SELECT id FROM weather_data ORDER BY timestamp DESC LIMIT 1)
                    """, (ac_status,))
                    conn.commit()
                print(f"에어컨 상태 변경: {ac_status}")
        
        time.sleep(7200)  # 2시간 대기

# 메인 페이지 라우트 추가
@app.route('/')
def index():
    return render_template('index.html')


# 실내 온습도 데이터를 위한 새로운 테이블 생성
def create_tables():
    with conn.cursor() as cur:
        # 기존 weather_data 테이블 유지
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id SERIAL PRIMARY KEY,
                temperature FLOAT NOT NULL,
                humidity FLOAT NOT NULL,
                discomfort_index FLOAT NOT NULL,
                ac_status VARCHAR(3) DEFAULT 'OFF',
                timestamp TIMESTAMP NOT NULL
            )
        """)
        
        # 실내 온습도 데이터를 위한 새로운 테이블
        cur.execute("""
            CREATE TABLE IF NOT EXISTS indoor_data (
                id SERIAL PRIMARY KEY,
                temperature FLOAT NOT NULL,
                humidity FLOAT NOT NULL,
                timestamp TIMESTAMP NOT NULL
            )
        """)
        conn.commit()

# 아두이노에서 받은 데이터를 저장하는 새로운 라우트
@app.route('/update_indoor_data', methods=['POST'])
def update_indoor_data():
    try:
        data = request.get_json()
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO indoor_data (temperature, humidity, timestamp)
                VALUES (%s, %s, (NOW() AT TIME ZONE 'Asia/Vientiane'))
            """, (temperature, humidity))
            conn.commit()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 실내 데이터를 가져오는 라우트 수정
@app.route('/get_indoor_data')
def get_indoor_data():
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT 
                temperature,
                humidity,
                to_char(timestamp AT TIME ZONE 'Asia/Vientiane', 'YYYY-MM-DD HH24:MI:SS') as timestamp
            FROM indoor_data
            WHERE timestamp >= NOW() - INTERVAL '6 hours'
            ORDER BY timestamp ASC
        """)
        data = cur.fetchall()
        return jsonify(data)

if __name__ == '__main__':
    create_table()  # 테이블 생성 함수 호출
    from threading import Thread
    weather_thread = Thread(target=periodic_updates)
    weather_thread.daemon = True
    weather_thread.start()
    app.run(host='0.0.0.0', port=5002)
