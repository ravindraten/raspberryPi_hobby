#!Vibration sensor to detect vibration and switch on leds depending on the bouncetime. ( SW-420 Vibration sensor)
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
green = 6
red = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0)

def callback(channel):
        if GPIO.input(channel):
                print "Movement Detected! 1"
                GPIO.output(green, 1)
                GPIO.output(red, 0)
        else:
                print "Movement Detected! 2"
                GPIO.output(red, 1)
                GPIO.output(green, 0)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=1000)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change



# infinite loop
while True:
       time.sleep(1)