import requests

TOKEN = "7716903147:AAHH67-STADFwfLwSdjs0Fbcaj1QWWhgUmE"
chat_id = "1485493857"
message = "Sending a Telegram message from Python code..."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

response = requests.get(url)
print(response.json())
