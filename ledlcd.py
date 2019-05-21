#!/usr/bin/python  
from firebase import firebase
firebase =firebase.FirebaseApplication('https://ras1-85ff0.firebaseio.com/',None)
r1=firebase.get('/user','Lane1')
r2=firebase.get('/user','Lane2')
r3=firebase.get('/user','Lane3')
r4=firebase.get('/user','Lane4')

import RPi.GPIO as GPIO  
from time import sleep  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class HD44780:  
  
    def __init__(self, pin_rs=7, pin_e=8, pins_db=[25, 24, 23, 18]):  
  
        self.pin_rs=pin_rs  
        self.pin_e=pin_e  
        self.pins_db=pins_db  
  
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.pin_e, GPIO.OUT)  
        GPIO.setup(self.pin_rs, GPIO.OUT)  
        for pin in self.pins_db:  
            GPIO.setup(pin, GPIO.OUT)  
  
        self.clear()  
  
    def clear(self):  
        """ Blank / Reset LCD """  
  
        self.cmd(0x33) # $33 8-bit mode  
        self.cmd(0x32) # $32 8-bit mode  
        self.cmd(0x28) # $28 8-bit mode  
        self.cmd(0x0C) # $0C 8-bit mode  
        self.cmd(0x06) # $06 8-bit mode  
        self.cmd(0x01) # $01 8-bit mode  
  
    def cmd(self, bits, char_mode=False):  
        """ Send command to LCD """  
  
        sleep(0.001)  
        bits=bin(bits)[2:].zfill(8)  
  
        GPIO.output(self.pin_rs, char_mode)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i], True)  
  
        GPIO.output(self.pin_e, True)  
        GPIO.output(self.pin_e, False)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4,8):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i-4], True)  
  
  
        GPIO.output(self.pin_e, True)  
        GPIO.output(self.pin_e, False)  
  
    def message(self, text):  
        """ Send string to LCD. Newline wraps to second line"""  
  
        for char in text:  
            if char == '\n':  
                self.cmd(0xC0) # next line  
            else:  
                self.cmd(ord(char),True)  
    

if __name__ == '__main__':
    lcd = HD44780() 
    GPIO.setup(15,GPIO.OUT)#green1
    GPIO.setup(17,GPIO.OUT)#green2
    GPIO.setup(22,GPIO.OUT)#green3
    GPIO.setup(9,GPIO.OUT)#green4

GPIO.setup(14,GPIO.OUT)#red1
GPIO.setup(27,GPIO.OUT)#red2
GPIO.setup(10,GPIO.OUT)#red3
GPIO.setup(11,GPIO.OUT)#

GPIO.output(15,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(9,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.output(11,GPIO.LOW)

GPIO.output(9,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(15,GPIO.HIGH)

GPIO.output(27,GPIO.HIGH)
GPIO.output(10,GPIO.HIGH)
GPIO.output(11,GPIO.HIGH)

for i in range(0,r1):
  sleep(1)
  a=r1-i
  if(a==5):
    lcd.message("BE READY TO STOP\n")
    sleep(0.5)
  lcd.message(str(a))
  sleep(0.5)
  lcd.clear()
  
	
GPIO.output(15,GPIO.LOW)

GPIO.output(14,GPIO.HIGH)
GPIO.output(27,GPIO.LOW)
GPIO.output(17,GPIO.HIGH)
for i in range(0,r2):
  sleep(1)
  a=r2-i
  if(a==5):
    lcd.message("BE READY TO STOP\n")
    sleep(0.5)
  lcd.message(str(a))
  sleep(0.5)
  lcd.clear()



GPIO.output(22,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.HIGH)
for i in range(0,r3):
  sleep(1)
  a=r3-i
  if(a==5):
    lcd.message("BE READY TO STOP\n")
    sleep(0.5)
  lcd.message(str(a))
  sleep(0.5)
  lcd.clear()



GPIO.output(9,GPIO.HIGH)
GPIO.output(11,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

GPIO.output(10,GPIO.HIGH)
for i in range(0,r4):
  sleep(1)
  a=r4-i
  if(a==5):
    lcd.message("BE READY TO STOP\n")
    sleep(0.5)
  lcd.message(str(a))
  sleep(0.5)
  lcd.clear()


GPIO.cleanup()
