import requests
import json

resp=requests.get("https://api.thingspeak.com/channels/1385393/feeds.json?api_key=ROUE9CVGCQQUA50T&results=10")

results=json.loads(resp.text)

for x in range(10):
    print("Download sample",x,": temperature =",results["feeds"][x]["field1"],", humidity =",results["feeds"][x]["field2"])
