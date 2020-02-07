import pprint
import telebot
import requests
from telebot.types import Message

TG_TOKEN = "1071984975:AAH2rEuvVpcStNlqAPvxpNuUjeiKyOEY2fw"
BASE_URL = f"https://api.telegram.org/bot{TG_TOKEN}/"

# r = requests.get(f"{BASE_URL}getMe")
# pprint.pprint(r.json())
# x = requests.get(f"{BASE_URL}getUpdates")
# pprint.pprint(x.json())
# pprint.pprint(x.json()["result"][-1])
#
# payload = {"chat_id": 360279278, "text": "Hi !"}
#
# y = requests.post(f"{BASE_URL}sendMessage", payload)
# pprint.pprint(y.json())
#
# l_payload = {"chat_id": 360279278, "latitude": 0.0809766, "longitude": 0.27826525}
# z = requests.post(f"{BASE_URL}sendLocation", l_payload)

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())


bot.polling()
