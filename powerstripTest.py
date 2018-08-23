#!/usr/bin/env python3

#powerstripTest allows simulation of the powerstrip module when not on a Raspberry Pi

import time

gpio_pin = False

def turn_off(seconds=0):
    global gpio_pin
    if(seconds > 0):
        if(not gpio_pin):
            print ('off')
            gpio_pin = not gpio_pin
        time.sleep(seconds)
        print ('on')
        gpio_pin = not gpio_pin
    else:
        if(not gpio_pin):
            print ('off')
            gpio_pin = not gpio_pin
            
def turn_on(seconds=0):
    global gpio_pin
    if(seconds > 0):
        if(gpio_pin):
            print ('on')
            gpio_pin = not gpio_pin
        time.sleep(seconds)
        print ('off')
        gpio_pin = not gpio_pin
    else:
        if(gpio_pin):
            print ('on')
            gpio_pin = not gpio_pin

def toggle():
    global gpio_pin
    if gpio_pin:
        print ('on')
    else:
        print ('off')
    gpio_pin = not gpio_pin
