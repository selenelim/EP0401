import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import requests

sensor = Adafruit_DHT.AM2302
pin = 4  # GPIO 4 (Physical Pin 7)
myUploadAPI = "0C1HPP56VI0QCKHI"

# Base URL for ThingSpeak API
baseURL = 'https://api.thingspeak.com/update'

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}°C  Humidity={1:0.1f}%'.format(temperature, humidity))
        
        # Send data to ThingSpeak
        payload = {
            'api_key': myUploadAPI,
            'field1': temperature,
            'field2': humidity
        }
        try:
            response = requests.get(baseURL, params=payload)
            print("Uploaded to ThingSpeak, response code:", response.status_code)
        except Exception as e:
            print("Error while uploading:", e)
    else:
        print('Failed to get reading. Try again!')

    sleep(15)  # Wait 15 seconds to comply with ThingSpeak's rate limit
