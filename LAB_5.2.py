#LAB5.2
import requests

# Replace this with your bot token
bot_token = '7716903147:AAHH67-STADFwfLwSdjs0Fbcaj1QWWhgUmE'

# Get updates (messages sent to your bot)
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

response = requests.get(url)

print(response.json())
