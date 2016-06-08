import requests
import RPi.GPIO as GPIO
import time
import sys

url ="localhost:3412"

if len(sys.argv) > 1:
    base_url = sys.argv[1]

# Setup things
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO_OUT)



def get_status():
    url = "http://{}/status".format(base_url)
    r = requests.get(url)
    result = r.json()
    return result['status']

def monitor_status():
    while True:
        time.sleep(0.3)
        status = get_status()
        print "Got status {}".format(status)
        if status == "on":
            GPIO.output(18,GPIO.HIGH)
        if status == "off":
            GPIO.output(18,GPIO.LOW)

monitor_status()
