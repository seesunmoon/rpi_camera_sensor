import RPi.GPIO as GPIO 
import subprocess 
from datetime import datetime 
import time 

movie_length = 10 # The length of the movie in seconds 

GPIO.setmode(GPIO.BOARD) 
pir = 7 # Change to your connected GPIO pin 
GPIO.setup(pir, GPIO.IN) 

print "Sensor initialized at " + str(datetime.now()) 
time.sleep(3) 

print "Detecting motion at " + str(datetime.now()) 

while True:
    if GPIO.input(pir):
      print "---"
      print "Motion Detected at " + str(datetime.now())
      print "Recording a movie for " + str(movie_length) + " seconds"
      subprocess.call(["gphoto2", "--set-config", "movie=1", "--wait-event=" + str(movie_length) + "s", "--set-config", "movie=0"])
      print "Hold 3 seconds"
      time.sleep(3)
      print "Finish recording and detecting motion again at " + str(datetime.now())
    time.sleep(0.5) # Detect motion every half second
  
