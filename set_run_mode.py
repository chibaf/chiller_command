#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import time

ser = serial.Serial(
    port='/dev/ttyUSB0',  # ポート名は環境に合わせて変更
    baudrate=9600,
    timeout=1  # タイムアウトの設定
)

#time.sleep(1)

# データ送信 
request_00S1 = b'\x04\x30\x30\x02\x4A\x4F\x30\x03\x37'
print(request_00S1)
ser.write(request_00S1)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
