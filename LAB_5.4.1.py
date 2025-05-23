import requests

TOKEN = "put token here"
chat_id = "put chat id here"
message = "Sending a Telegram message from Python code..."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

response = requests.get(url)
print(response.json())
