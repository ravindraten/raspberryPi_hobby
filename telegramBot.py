import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
from time import sleep
from sys import exit

white = 26
blue = 19
red = 13
green = 6
buzzer = 23

now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 
LED White
GPIO.setup(white, GPIO.OUT)
GPIO.output(white, 0) #Off initially
LED Blue
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, 0) #Off initially
LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially
Buzzer
GPIO.setup(buzzer, GPIO.OUT)


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Received: %s' % command)
    if 'how are you?' in command:
        message = "I am good .. How are you?"
        telegram_bot.sendMessage (chat_id, message)
        
    if 'hello' in command:
        message = ("Hello , How can i help you?"+
        " Use these commands to make the best use of me"+
                  " To switch on a light: Ex: 'Turn on Red light.'"+
                  " Currently I have 4 lights which you can play with :)")
        telegram_bot.sendMessage (chat_id, message)
        telegram_bot.sendSticker (chat_id, "https://www.gstatic.com/webp/gallery/5.webp")

        
    if 'on' in command:
        message = "Turned on "
        if 'white' in command:
            message = message + "white light"
            GPIO.output(white, 1)
        if 'blue' in command:
            message = message + "blue light"
            GPIO.output(blue, 1)
        if 'red' in command:
            message = message + "red light"
            GPIO.output(red, 1)
        if 'green' in command:
            message = message + "green light"
            GPIO.output(green, 1)
        if 'all' in command:
            message = message + "all lights"
            GPIO.output(white, 1)
            GPIO.output(blue, 1)
            GPIO.output(red, 1)
            GPIO.output(green, 1)
        if 'buzzer' in command:
            telegram_bot.sendMessage (chat_id, "Buzzer starting to beep...")
            for x in range(5):
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(0.5) # Delay in seconds
                GPIO.output(buzzer,GPIO.LOW)
                sleep(0.5)
            message = "Beeping stopped "
        message = message
        telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'white' in command:
            message = message + "white "
            GPIO.output(white, 0)
        if 'blue' in command:
            message = message + "blue "
            GPIO.output(blue, 0)
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 0)
        if 'green' in command:
            message = message + "green "
            GPIO.output(green, 0)
        if 'all' in command:
            message = message + "all "
            GPIO.output(white, 0)
            GPIO.output(blue, 0)
            GPIO.output(red, 0)
            GPIO.output(green, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)
    
    if 'blink' in command:
        message = "Blinking "
        if 'white' in command:
            message = message + "white "
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
            for x in range(5): #blink 5 times
                GPIO.output(white, True) #turn on
                sleep(1)
                GPIO.output(white, False) #turn off
                sleep(1)
        if 'blue' in command:
            message = message + "blue "
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
            for x in range(5): #blink 5 times
                GPIO.output(blue, True) #turn on
                sleep(1)
                GPIO.output(blue, False) #turn off
                sleep(1)
        if 'green' in command:
            message = message + "green "
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
            for x in range(5): #blink 5 times
                GPIO.output(green, True) #turn on
                sleep(1)
                GPIO.output(green, False) #turn off
                sleep(1)
        if 'red' in command:
            message = message + "red "
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
            for x in range(5): #blink 5 times
                GPIO.output(red, True) #turn on
                sleep(1)
                GPIO.output(red, False) #turn off
                sleep(1)
        if 'all' in command:
            message = message + "all "
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
            for x in range(5): #blink 5 times
                GPIO.output(red, True) #turn on
                sleep(1)
                GPIO.output(blue, True) #turn off
                sleep(1)
                GPIO.output(green, True) #turn on
                sleep(1)
                GPIO.output(white, True) #turn off
                sleep(1)
                GPIO.output(red, False) #turn on
                sleep(1)
                GPIO.output(blue, False) #turn off
                sleep(1)
                GPIO.output(green, False) #turn on
                sleep(1)
                GPIO.output(white, False) #turn off
                sleep(1)   
        message = "Blinking stopped"
        telegram_bot.sendMessage (chat_id, message)
        
        #telegram_bot.sendPhoto (chat_id, open('/home/pi/Documents/Telegram/Family.jpeg'))
        
       
telegram_bot = telepot.Bot('') #API key from telegram
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)
