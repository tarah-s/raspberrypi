# External module imports
import os
import RPi.GPIO as GPIO
import time
import subprocess
import url
import calendar
import json

os.system("sudo amixer sset PCM,0 300%")

BatteryTime = # hours

url = ''
postdata = { 'time': str(calendar.timegm(time.gmtime())) }
req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)


butPin = 17 # Broadcom pin 17 (P1 pin 11)

# Pin Setup:
GPIO.setmode(GPIO.BCM)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Here we go! Press CTRL+C to exit")
buttonCount = 0


while True:
   input_state = GPIO.input(17)
   if input_state == False:
      os.system('date')
      subprocess.call('bash /home/pi/Desktop/trolley/playsound.sh', shell=True)
      buttonCount = buttonCount + 1
      print('Number:',buttonCount)
      response = urllib2.urlopen(req,data)
      time.sleep(0.75)

