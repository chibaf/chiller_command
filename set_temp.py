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

# データ送信  温度設定
request_00S1 = b'\x04\x30\x30\x02\x4A\x4F\x31\x03\x37'
ser.write(request_00S1)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)

S1_25=b'\x04\x30\x30\x02\x53\x31\x20\x20\x20\x20\x32\x35\x2E\x30\x03\x7D'
ser.write(S1_25)

# データ受信
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
