#!/usr/bin/env python

import telebot
bot_token = "Your bot token" # add your telegram bot token

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])

def wlcm_msg(message):
    wlcm_text = """welcom to chat id bot send /id command to know your id
    created by @alienkrishn""" # add your username 
    bot.reply_to(message, wlcm_text)

@bot.message_handler(commands=['id'])
def send_id(message):
    chat_id = message.chat.id 
    bot.reply_to(message, f"Your chat id is : {chat_id}")
bot.polling()
