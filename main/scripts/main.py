from .translate import *
from . import constants
from telebot import apihelper


def handler_text(message):
    text = str(detect_text(message.text)['lang'])
    if text == 'en':
        bot.send_message(message.chat.id, get_translate(message.text, 'ru')['text'])
    #       print(get_translate(text, 'ru')['text'])
    elif text == 'ru':
        bot.send_message(message.chat.id, get_translate(message.text, 'en')['text'])
    #      print(get_translate(text, 'en')['text'])
    else:
        bot.send_message(message.chat.id, 'Иди на хуй! Тебе не надо переводить этот текст.')


#while True:
#    try:
bot.polling(none_stop=True, interval=0, timeout=20)
#    except Exception as E:
#        print(E.args)
#        time.sleep(20)
