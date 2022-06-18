import telebot
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telebot import types

# pip install python-telegram-bot - загрузить библиотеку
# t.me/team_phonebook_bot -- ссылка на наш бот, pnonebook_bot - name, team_phonebook_bot

bot = Bot(token='5570893886:AAHBpHJ83y6EIx3CiNklHhMgXcZpbTaUcQs')
updater = Updater(token='5570893886:AAHBpHJ83y6EIx3CiNklHhMgXcZpbTaUcQs', use_context=True)
dispatcher = updater.dispatcher

# @bot.message_handler(commands=['start'])
def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")




def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создала компания GB!")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ты несешь какую-то дичь...')


# start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown) #/game

# dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


print("server_started")

updater.start_polling()
updater.idle()