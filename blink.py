import RPi.GPIO as GPIO     # Importing the GPIO library to use the GPIO pins of Raspberry pi
import time, datetime
import telepot
from telepot.loop import MessageLoop
from time import sleep
from sys import exit# Importing the time library to provide the delays in program

led_pin = 26                # Initializing pin 21 for led

GPIO.setmode(GPIO.BCM)      # Using BCM numbering
GPIO.setup(led_pin, GPIO.OUT) # Declaring the pin 21 as output pin

for x in range(5):             # Loop will run only five times
    GPIO.output(led_pin, True) # Turn LED ON
    print ('LED ON')
    sleep(1)                   # Delay of 1 sec
    GPIO.output(led_pin, False) # Turn LED OFF
    print('LED OFF')
    sleep(1)                    # Delay of 1 sec
    
GPIO.cleanup()                  # Making all the output pins LOW