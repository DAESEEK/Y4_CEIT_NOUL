# app.py
from flask import Flask, render_template, request
import serial
import time

app = Flask(__name__)

# 아두이노가 연결된 시리얼 포트 설정 (예: '/dev/tty.usbmodem14101')
arduino = serial.Serial('/dev/cu.usbserial-141220', 9600)  # 포트는 Mac에서 연결된 포트를 확인하세요.
time.sleep(2)  # 시리얼 연결 안정화 대기

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led', methods=['POST'])
def led():
    status = request.form['status']
    if status == 'on':
        arduino.write(b'1')  # LED 켜기 명령 전송
    elif status == 'off':
        arduino.write(b'0')  # LED 끄기 명령 전송
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
