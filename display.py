import os
import time
import psutil
import socket
import Adafruit_CharLCD as LCD
from datetime import datetime

#Display info
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 4


lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

def measure_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=",""))

while True:
	#CPU usage + temp
	ora=time.time()
	fine=ora+10.0
	while(time.time()<=fine):
		CPU_usage = psutil.cpu_percent (interval=1)
		CPU_show = str(CPU_usage)
		lcd.clear()
		lcd.home()
		lcd.message('CPU usage: ')
		lcd.message(CPU_show)
		lcd.set_cursor(15, 0)
		lcd.message('%')
		lcd.set_cursor(1, 1)
		lcd.message("{}".format(time.strftime("%d-%m %H:%M:%S")))
		time.sleep(1.0)
	#RAM usage + temp
	ora=0
	fine=0
	ora=time.time()
	fine=ora+6
	while(time.time()<=fine):
		RAM_usage = psutil.virtual_memory()[2]
		RAM_show = str(RAM_usage)
		lcd.clear()
		lcd.home()
		lcd.message('RAM usage: ')
		lcd.message(RAM_show)
		lcd.set_cursor(15, 0)
		lcd.message('%')
		lcd.set_cursor(0, 1)
		lcd.message('CPU Temp: ')
		lcd.message(measure_temp())
		time.sleep(1.0)
