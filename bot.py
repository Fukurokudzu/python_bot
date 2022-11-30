# THIS IS BASIC ECHO TELEGRAM BOT, BASED ON https://github.com/python-telegram-bot v20

import logging
from telegram import Update
import datetime
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
# you should create config.py file next to the script
# past this text (without hashtags) there:
#
# settings = {
#     'token':'TOKEN_YOU_GOT_FROM_GODFATHER_BOT'
# }

import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def echo_text(text):
    new_text = "Echo" + text
    return new_text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hi. I send the same message"
                                   "back to you, that's all for now")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=echo_text(update.message.text))
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"), update.message.text, "->",
          echo_text(update.message.text))

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=text_caps)

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.settings['token']).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    caps_handler = CommandHandler('caps', caps)
    application.add_handler(caps_handler)

    application.run_polling()