# ALS Bengaluru
# Program to capture a image form pi camera
#connect a Pi camera. and Enable camera from Raspberry pi configuaration
#All the captured images will be stored at /home/pi/MCASyllabus/images folder.

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()


camera.start_preview()

current_date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

sleep(5)

camera.capture('/home/pi/Desktop/'+current_date+'.jpg')

camera.stop_preview()

print("Image captured")

#sleep(2)
