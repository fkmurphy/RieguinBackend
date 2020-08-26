import telebot
from telebot import types
#import logging
import requests


import os
import sys
from time import sleep

#ENV=env.read(".env")
#bot = telebot.TeleBot(ENV['TELEGRAM_BOT_API_KEY'])
#bot = None

# parametros para conexion con telegram
BOT_TIMEOUT=3
BOT_INTERVAL=5

URL="http://web:8000/"
#logging.basicConfig(filename='bitacora-bot.log',filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def bot_polling():
    #global bot
    print("Comenzando")
    while True:
        try:
            # intentar conectar a telegram
            #bot = telebot.TeleBot
            bot = telebot.TeleBot(os.environ.get('API_KEY','NONE'))
            botactions(bot)
            bot.polling(none_stop=True,interval=BOT_INTERVAL,timeout=BOT_TIMEOUT)
        except Exception as ex:
            print("Error")
            bot.stop_polling()
            sleep(BOT_TIMEOUT)
        else:
            print("hubo un error")
            bot.stop_polling()
            break

def botactions(bot):
    @bot.message_handler(commands=['start'])
    def index(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(commands=['i'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('lightUp','lightDown','Hum','lightStatus','fanStatus','fanDown','fanUp')
        msg = bot.send_message(message.chat.id,'select option',reply_markup=markup)
        bot.register_next_step_handler(message,process)
    def selectDownFan(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('salida','entrada','interno')
        msg = bot.reply_to(message,'select option',reply_markup=markup)
        bot.register_next_step_handler(message,downFan)
    def downFan(message):
        cid = message.chat.id
        if(message.text == u'salida'):
            idFan=3
        elif(message.text == u'entrada'):
            idFan=27
        elif(message.text == u'interno'):
            idFan=17
        r = requests.get(url=URL+"luz/up/"+str(idFan)+"/")
        data = ""
        if (r.status_code == 200):
            data = r.text
        bot.reply_to(message,data)
        #bot.register_next_step_handler(message,start)
        start(message)
    def selectUpFan(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('salida','entrada','interno')
        msg = bot.reply_to(message,'select option',reply_markup=markup)
        bot.register_next_step_handler(message,upFan)
    def upFan(message):
        cid = message.chat.id
        if(message.text == u'salida'):
            idFan=3
        elif(message.text == u'entrada'):
            idFan=27
        elif(message.text == u'interno'):
            idFan=17
        r = requests.get(url=URL+"luz/down/"+str(idFan)+"/")
        data = ""
        if (r.status_code == 200):
            data = r.text
        bot.reply_to(message,data)
        #bot.register_next_step_handler(message,start)
        start(message)
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def process(message):
        cid=message.chat.id
        reply=message.text
        if(reply == u'Hum'):
            r = requests.get(url=URL+"hum/")
            data=""
            print(str(r.status_code))
            if(r.status_code == 200):
                data = r.text
            print(str(data))
            bot.send_message(cid,data)
        elif (reply == 'lightUp' ):
            r = requests.get(url=URL+"luz/down/2/")
            data = ""
            if (r.status_code == 200):
                data = r.text
            bot.send_message(cid,data)
        elif (reply == 'lightDown'):
            r = requests.get(url=URL+"luz/up/2/")
            data = ""
            if (r.status_code == 200):
                data = r.text
            bot.send_message(cid,data)
        elif (reply == 'fanDown'):
            selectDownFan(message)
        elif (reply == 'fanUp'):
            selectUpFan(message)
        elif (reply == 'lightStatus'):
            r = requests.get(url=URL+"luz/status/2/")
            data = ""
            if (r.status_code == 200):
                data = r.text
            bot.send_message(cid,data)
        elif (reply == 'fanStatus'):
            r = requests.get(url=URL+"luz/status/3/")
            data = ""
            if (r.status_code == 200):
                data = r.text
            bot.send_message(cid,data)
        




bot_polling()
