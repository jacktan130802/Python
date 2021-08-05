import time
import requests

temperature=[23,24,25,23,21,22,24,26,27,26]
humidity=[55,57,60,59,62,66,70,68,66,65]

for x in range(10):
    print("Uploading sample",x,"...")
    resp=requests.get("https://api.thingspeak.com/update?api_key=SDDXQHICM6BQR8H8&field1=%s&field2=%s"%(temperature[x],humidity[x]))
    time.sleep(20)                 
