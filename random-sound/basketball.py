# External module imports
import os
import RPi.GPIO as GPIO
import time
import subprocess
from firebase import firebase
 
 
butPin = 17 # Broadcom pin 17 (P1 pin 11)
 
# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
 
scoreCount = 0

print("Here we go! Press CTRL+C to exit")
firebase = firebase.FirebaseApplication('https://', None)
buttonCount = 0 

 
while True:
   input_state = GPIO.input(17)
   if input_state == False:
      os.system('date')
      subprocess.call('bash playsound.sh', shell=True)
      buttonCount = buttonCount + 1
      print('Number:',buttonCount)
      result = firebase.post('/scoreboard',{'Score': buttonCount})
      print result
      time.sleep(0.75