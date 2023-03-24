# ALS Bengaluru
# Program to Take input from two switches and switch on corresponding LEDs.
# Connect J4A PIN-1,2,3,4,5 TO J4 PIN-1,2,3,4,5
# Dont forget to short the jumper JP1
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD) 

led1 = 15  #P15    # pin is connected to LED and it should be OUT
led2 = 13  #P13     # pin is connected to LED and it should be OUT
switch1 = 37      #P37  # pin is connected to SWITC and it should be IN
switch2 = 35      #P35 # pin is connected to SWITC and it should be IN

gpio.setup(led1,gpio.OUT,initial=1)
gpio.setup(led2,gpio.OUT,initial=1)
gpio.setup(switch1,gpio.IN)
gpio.setup(switch2,gpio.IN)

def glow_led(event):
    if event == switch1 :
        gpio.output(led1, False)
        time.sleep(3)
        gpio.output(led1, True)
    
    elif event == switch2 :
        gpio.output(led2, False)
        time.sleep(3) 
        gpio.output(led2, True)
        
gpio.add_event_detect(switch1, gpio.RISING , callback = glow_led, bouncetime = 1)
gpio.add_event_detect(switch2, gpio.RISING , callback = glow_led, bouncetime = 1)

try:
    while(True):
    #to avoid 100% CPU usage
       time.sleep(1)
except KeyboardInterrupt:
    #cleanup GPIO settings before exiting
    gpio.cleanup()

