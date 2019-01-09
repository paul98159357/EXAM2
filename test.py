#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
while True:
    LEDon = GPIO.output(23, 1)   #LED燈亮
    print ("LED on GPIO-23 is on")
    time.sleep(1)
    LEDoff = GPIO.output(23,0)   #LED燈熄
    print ("LED on GPIO-23 is off")
    time.sleep(1)

