import os
import telebot


bot = telebot.TeleBot("5186367071:AAGdGJo5twcBdhK4W8GchA-JHcCN1GdGGl4")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()
