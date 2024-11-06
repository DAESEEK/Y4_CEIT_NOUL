from pyfirmata2 import Arduino
import serial
import time

ser = serial.Serial('/dev/cu.usbserial-141220', 115200)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
