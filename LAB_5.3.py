import json
import requests

resp = requests.get("https://api.thingspeak.com/channels/2970897/feeds.json?results=10")
#print(resp.text)
results=json.loads(resp.text)

for x in range (10):
    print("temperature: ",results ["feeds"][x]["field1"],", humidity: ",results ["feeds"][x]["field2"])