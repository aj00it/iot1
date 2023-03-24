# ALS Bengaluru
# Program to controlling a light source using web page
#install the following command in terminal
#sudo apt-get install python3-flask
# Create a folder "templates" and write your html pages in this folder.

import RPi.GPIO as GPIO 
import time
import datetime

led = 13 #P15

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(led, GPIO.OUT,initial=0) #Initialising GPIO pins as output
GPIO.setup(led,GPIO.OUT)

from flask import Flask, render_template #Importing Flask

app = Flask(__name__)

@app.route('/') #Simple Hello World Route
def hello_world():
    return render_template('web.html')
    

@app.route('/redledon') #Route for Turning RedLed On
def redledon():
    
    GPIO.output(13, GPIO.LOW) #Turning Pin 31 --> Red Led HIGH
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'status' : 'ON',
      'time': timeString
      }
    return render_template('web.html', **templateData)

@app.route('/redledoff') #Route for Turning RedLed Off
def redledoff():
    GPIO.output(13, GPIO.HIGH)  #Turning Pin 31 --> Red Led LOW
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'status' : 'OFF',
      'time': timeString
      }
    return render_template('web.html', **templateData)

if __name__ == "__main__":
    app.run(debug = True, port = 4000, host='0.0.0.0')
