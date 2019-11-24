import sys
import serial 
import RPi.GPIO as GPIO 
import I2C_LCD_driver  
GPIO.setmode(GPIO.BCM)
from time import *

mylcd = I2C_LCD_driver.lcd()

def start():
	mylcd.lcd_display_string("Welcome",1)
	mylcd.lcd_display_string("Tap Your Card",2)
	Tag1 = str('6D003E1A1A53')
	PortRF = serial.Serial('//dev/ttyUSB0',9600)
        Log = ""
	while True:
		ID = ""
		read_byte = PortRF.read()
    	        if read_byte=="\x02":
        		for Counter in range(12):
                    		read_byte=PortRF.read()
                    		ID = ID + str(read_byte)
                    		print hex(ord( read_byte))
	        	mylcd.lcd_clear()
			print ID
			if ID == Tag1:
            	   		mylcd.lcd_display_string("Access",1)
				mylcd.lcd_display_string("Successful",2)
            	   		sleep(5)
                                mylcd.lcd_clear()
        		else:
            	   		mylcd.lcd_display_string("Access",1)
				mylcd.lcd_display_string("Denied",2)
                   		sleep(5)
				mylcd.lcd_clear()
			break

for _ in range(99999):
    start()
