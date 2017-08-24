import datetime, time
import urllib.request
import random

myurl = "https://api.thingspeak.com/update?api_key=1ACQYGKVX7EBBG3S&field1=0"

for i in range(20):
    myurl += str(random.randint(20,80))
    f=urllib.request.urlopen(myurl)
    data = str(f.read)
    print("got ", data)
    time.sleep(15)
    
