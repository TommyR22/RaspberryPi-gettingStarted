# @author TommasoRuscica
#
# Telegram and raspberry
#
# ----------------------

# -*- coding: utf-8 -*-

# libraries
import sys
import time
import random
import datetime
import telepot
import dht11
import RPi.GPIO as GPIO

# initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# read data using pin 14
instance = dht11.DHT11(pin=4)

def read():
    result = instance.read()
    if result.is_valid():
        text = "Last valid input: " + str(datetime.datetime.now()) + "\nTemperature: " + str(result.temperature) +"°"+ "\nHumidity: " + str(result.humidity) +"%"
        
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        
        return text
    else:
        return "Please retry.."
    

def handle(msg):
    chat_id = msg['chat']['id']
    
    if 'text' in msg:
        command = msg['text']
        print 'Got command: %s' % command
        if command == 'Temp':
            text = read()
            bot.sendMessage(chat_id, text)
        elif command == 'Get':
            f = open('/home/pi/projects/prova.png', 'rb')  
            response = bot.sendPhoto(chat_id, f)
        else:
            bot.sendMessage(chat_id, "Unrecognized command")

    #elif command =='off':
    #  bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('336394970:AAFLSLIV_UCAR8_KdH9Ra9_tV3PLUWnwW2Q')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
