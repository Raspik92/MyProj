import requests
import access


TOKEN = access.TOKEN


url = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"

response = requests.get(url)
data = response.json()

print("Webhook info:")
print(data)