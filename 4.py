# ALS Bengaluru
# Program to switch on relay at given time using cron. 
# Set crontab -e.
#minute Hour Day of the month month Day of the week <command to execute>
#example
#0 12 13 * * python3 /home/pi/MCASyllabus/10.py

import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD) 

relay1 = 38    #P38
gpio.setup(relay1,gpio.OUT,initial=0)  

try:
	gpio.output(relay1, True)
	print("Relay is Switched On. Please Press ctrl+c to exit")
	time.sleep(5)
	print("Relay is Switched Off.")
	gpio.output(relay1, False)
except KeyboardInterrupt:
	gpio.cleanup()
	print("Program Exited")
