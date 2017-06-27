# @author TommasoRuscica
#
# LED
#
# ----------------------

# import libraries
import RPi.GPIO as GPIO         
import time

# set pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# configure channels as input or output
# button connected on pin 4.
# led connected on pin 17.
GPIO.setup(4,GPIO.IN)
GPIO.setup(17,GPIO.OUT)

# to declare multiple channel of same type
# chan_list = [11,12]    
# GPIO.setup(chan_list, GPIO.OUT)

while True:
    button = GPIO.input(4)
    if button:
        print('led on')
        time.sleep(0.2)
        GPIO.output(17,True)  #or GPIO.output(17,GPIO.HIGH) or GPIO.output(17,1)
        # GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))         # sets first HIGH and second LOW

    else:
        print('led off')
        GPIO.output(17,False)        
        
# At the end any program, it is good practice to clean up any resources you might have used. 
# This is no different with RPi.GPIO. By returning all channels you have used back to inputs with no pull up/down, 
# you can avoid accidental damage to your RPi by shorting out the pins.
GPIO.cleanup()
