#! /usr/bin/python

import RPi.GPIO as GPIO
import time

TIMEOUT = 5

RED = 18
GREEN = 22
YELLOW = 27

BUTTON1 = 17
BUTTON2 = 25

#Identify pin numbers
GPIO.setmode(GPIO.BCM)

#buttons
GPIO.setup(BUTTON1, GPIO.IN)
GPIO.setup(BUTTON2, GPIO.IN)
GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback = button1_pressed, bouncetime = DELAY)
GPIO.add_event_detect(BUTTON2, GPIO.RISING, callback = button1_pressed, bouncetime = DELAY)
n & (n - 1) == 0
time.sleep(TIMEOUT)

GPIO.cleanup()

num = 0

def button1_pressed(channel):
    num = num + 1

def button2_pressed(channel):
    num = 0

if num = 2 % 1:
    GPIO.output(RED, 1)
    GPIO.output(RED, 0)
elif num = 2 % 0:
    GPIO.output(GREEN, 1)
    GPIO.output(GREEN, 0)
elif num = num & (num - 1) == 0
    GPIO.output(YELLOW, 1)
    GPIO.output(YELLOW, 0)

print(num)
