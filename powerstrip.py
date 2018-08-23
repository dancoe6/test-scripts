#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

gpio_pin = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
gpio_pin = GPIO.input(18)
GPIO.setup(18, GPIO.OUT)

def turn_off(seconds=0):
    global gpio_pin
    if(seconds > 0):
        if(not gpio_pin):
            GPIO.output(18, GPIO.HIGH)
            gpio_pin = not gpio_pin
        time.sleep(seconds)
        GPIO.output(18, GPIO.LOW)
        gpio_pin = not gpio_pin
    else:
        if(not gpio_pin):
            GPIO.output(18, GPIO.HIGH)
            gpio_pin = not gpio_pin
            
def turn_on(seconds=0):
    global gpio_pin
    if(seconds > 0):
        if(gpio_pin):
            GPIO.output(18, GPIO.LOW)
            gpio_pin = not gpio_pin
        time.sleep(seconds)
        GPIO.output(18, GPIO.HIGH)
        gpio_pin = not gpio_pin
    else:
        if(gpio_pin):
            GPIO.output(18, GPIO.LOW)
            gpio_pin = not gpio_pin

def toggle():
    global gpio_pin
    GPIO.output(18, (not gpio_pin))
    gpio_pin = not gpio_pin
