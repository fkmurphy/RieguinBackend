from django.shortcuts import render
import telebot

import Adafruit_DHT as dht
from telebot import types

DHTPIN=4
DHTSENSOR=dht.DHT22

API_TOKEN="1349541128:AAHjECE5m_MzGB8F50y0K68YjFTQx3_Q_eY"
#telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)
# Create your views here.

@bot.message_handler(commands=['start'])
def index(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['i'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('lightUp','lightDown','Hum')
    msg = bot.reply_to(message,'select option',reply_markup=markup)
    bot.register_next_step_handler(message,process)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def process(message):
    cid=message.chat.id
    reply=message.text
    if(reply == u'Hum'):
        humidity,temperature = dht.read_retry(DHTSENSOR,DHTPIN)
        if humidity is not None and temperature is not None:
            result ="temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity)
            bot.send_message(cid,result)
    elif (reply == 'lightUp' ):
        bot.send_message(cid,"No disponible")
    elif (reply == 'lightDown'):
        bot.send_message(cid, "No disponible")


bot.polling(none_stop=False, interval=0, timeout=20)
