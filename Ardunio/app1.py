# 아두이노에 1개의 LED를  Web에 연결하고 데이타베이스에 

from flask import Flask, render_template, request
import serial
import time

app = Flask(__name__)

# 아두이노가 연결된 시리얼 포트를 설정합니다. (예: '/dev/tty.usbmodem14101')
arduino = serial.Serial('/dev/cu.usbserial-14230', 9600)  # 실제 포트로 변경
time.sleep(2)  # 시리얼 연결 안정화 대기

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/led', methods=['POST'])
def led():
    color = request.form['color']
    action = request.form['action']
    command = f"{color.upper()}_{action.upper()}"
    arduino.write(command.encode())  # 명령어 전송
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)