#! /usr/bin/python

import RPi.GPIO as GPIO
import time

BUTTON1 = 17
BUTTON2 = 25
DELAY = 100
TIMEOUT = 10
YELLOW = 27

#Identify pin numbers
GPIO.setup(GPIO.BCM)

#Yellow Light
GPIO.setup(YELLOW, GPIO.OUT)

#Respond to BUTTON1
def button1_pressed(channel):
    #Turn on yellow Light
    GPIO.output(YELLOW, 1)

#Respond to BUTTON2
def button2_pressed(channel):
    #Turn of yellow light
    GPIO.output(YELLOW, 0)

#Inform pi that pin 17 will be used
GPIO.setup(BUTTON1, GPIO.IN)

#Implement DELAY for button1
GPIO.add_event_detect(BUTTON1,  GPIO.RISING, callback = button1_pressed, bouncetime = DELAY)

#Setup pin 25
GPIO.setup(BUTTON2, GPIO.IN)

#Implement delay for button2
GPIO.add_event_detect(BUTTON1,  GPIO.RISING, callback = button1_pressed, bouncetime = DELAY)

time.sleep(TIMEOUT)

# Turn off the yellow LED
GPIO.output(YELLOW, 0)

GPIO.cleanup()
