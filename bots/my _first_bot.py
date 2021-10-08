# обычный эхо-бот

from telebot import *
from config_my_first_bot import TOKEN 
        """ Импортируем все библиотеки , в том числе токен"""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])            # С этой функции приветствуем  пользователя
def start_message(message):
    bot.send_message(message.chat.id, "Привет, Даня. Я буду повторять все то что ты напишешь в этот чат!!")

@bot.message_handler(content_types = ['text'])      # С помощьб этой функции просто повторяем, то что напечатает юзер
def repeat_message(message):
    bot.send_message(message.chat.id, message.text) 


bot.infinity_polling()