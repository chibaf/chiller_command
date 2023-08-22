#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',  # ポート名は環境に合わせて変更
    baudrate=9600,
    timeout=1  # タイムアウトの設定
)

# データ送信  運転状態の送信の要求
request_00S1 = b'\x04\x30\x30\x02\x4A\x4F\x31\x03\x37'
ser.write(request_00S1)

# データ受信
line = ser.readline() 
print(line) 
line2 = line.strip().decode("utf-8")
print(line2)
