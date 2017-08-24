import datetime, time
import urllib.request
import random

myurl = "https://api.thingspeak.com/update?api_key=1ACQYGKVX7EBBG3S&field1="

for i in range(20):
    url = myurl + str(random.randint(20,80))
    print("myurl=", url)
    f=urllib.request.urlopen(url)
    data = str(f.read)
    print("got ", data)
    time.sleep(15)
    
