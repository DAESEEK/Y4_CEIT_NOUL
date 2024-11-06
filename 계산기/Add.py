import prserial
import time

ser = prserial.Serial('USB', 115200)

while True:
    if ser.in_waiting >0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)



