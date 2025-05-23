from PIL import Image
from io import BytesIO
import requests

# Telegram Bot token and chat ID
TOKEN = "7716903147:AAHH67-STADFwfLwSdjs0Fbcaj1QWWhgUmE"
chat_id = "665618214"

# 1. Send a text message
message = "Sending a Telegram message from Python code..."
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    'chat_id': chat_id,
    'text': message
}
print(requests.get(url, params=payload).json())

# 2. Send an image
# Make sure the image path is correct
img = Image.open("slowpoke.png")

# Prepare image for upload
image_stream = BytesIO()
img.save(image_stream, format='PNG')
image_stream.seek(0)

# Send image to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
files = {'photo': ('image.png', image_stream)}
data = {'chat_id': chat_id}
print(requests.post(url, files=files, data=data).json())
