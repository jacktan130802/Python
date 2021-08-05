import requests

resp=requests.post("https://api.thingspeak.com/apps/thingtweet/1/statuses/update",json={"api_key":"D6QNRFQ5BBVZKGWK","status":"Testing Python tweetbot..."})
