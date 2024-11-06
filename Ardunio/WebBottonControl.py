from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 초기 LED 상태
led_status = 'off'

@app.route('/')
def index():
    return render_template('index-1.html', status=led_status)

@app.route('/led', methods=['POST'])
def control_led():
    global led_status
    # 버튼 상태를 변경
    if led_status == 'off':
        led_status = 'on'
        print("Light on.")
    else:
        led_status = 'off'
        print("Light off")
    
    # 현재 LED 상태를 JSON으로 반환
    return jsonify({'status': led_status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # host와 port 설정 추가 