"""
Test LEDS

Script to test the ability to set the state of an LED attached to pin 16 on a Raspberry Pi GPIO.

Created: 02/07/2024
Author: Ze'ev Krischer & Michael Rubin
"""


import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

green = 16
red = 13
blue = 15

GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


def testLED():

    blink_status = False
    
    print("LED ON")
    i = 0
    while True:

        GPIO.output(green, 1)
        GPIO.output(red,1)
        GPIO.output(blue,1)
        if (i == 1000000):
            break

        i+=1

    print("LED OFF")
    GPIO.output(red,0)
    GPIO.output(blue,0)

if __name__ == "__main__":
    testLED()
