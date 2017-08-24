import RPi.GPIO as GPIO
import dht11
import time
import datetime
import urllib.request

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

myurl = "https://api.thingspeak.com/update?api_key=1ACQYGKVX7EBBG3S&field1={hum}&field2={temp}"
myurl2 = "http://192.168.0.7:5000/?field1={hum}&field2={temp}"


# read data using pin 14
instance = dht11.DHT11(pin=2)

while True:
    result = instance.read()
    if result.is_valid():
        url = myurl.format(hum=str(result.humidity), temp=str(result.temperature))
        url2 = myurl2.format(hum=str(result.humidity), temp=str(result.temperature))
        f=urllib.request.urlopen(url)
        f2=urllib.request.urlopen(url2)
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    time.sleep(15)
