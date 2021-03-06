from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = "1071984975:AAH2rEuvVpcStNlqAPvxpNuUjeiKyOEY2fw"


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = "anonim"
    text_ = update.effective_message.text
    reply_text = f"Hello, {name}!\n\n{text_}"

    bot.send_message(chat_id=update.effective_message.chat_id,
                     text=reply_text)


def main():
    print("Start!")
    bot = Bot(token=TG_TOKEN)
    updater = Updater(bot=bot)
    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
    print("Finish!")


if __name__  == "__main__":
    main()
