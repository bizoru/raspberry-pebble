import requests
import RPi.GPIO as GPIO
import time
import sys

# Setup things
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def get_status():
    url = "http://{}/status".format(url)
    r = requests.get(url)
    result = r.json()
    return result['status']

def monitor_status(url="localhost:3412"):
    while True:
        time.sleep(0.3)
        status = get_status()
        print "Got status {}".format(status)
        if status == "on":
            GPIO.output(18,GPIO.HIGH)
        if status == "off":
            GPIO.output(18,GPIO.LOW)

if len(sys.argv) > 1:
    base_url = sys.argv[1]
    monitor_status(base_url)
else:
    monitor_status()
