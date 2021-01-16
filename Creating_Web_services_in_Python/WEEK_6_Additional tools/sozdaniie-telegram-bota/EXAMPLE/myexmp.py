import time
import telebot
from telebot import apihelper
apihelper.proxy = {'https':'socks5://127.0.0.1:9150'}
bot = telebot.TeleBot('1154473055:AAFydNvT9RBeL8kAwdaXKEjst7mTr2qfLHk')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'ПРОВЕРКА', reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'ПРОВЕРКА')


data = []
@bot.message_handler(commands=['add'])
def add_place(message):
    bot.send_message(message.chat.id, 'ВВЕДИТЕ МЕСТО:')
    bot.register_next_step_handler(message, get_place)
def get_place(message):
    data.append(message.text);
    bot.send_message(message.from_user.id, 'ЗАПИСАНО')
@bot.message_handler(commands=['list'])
def list_of_place(message):
    bot.send_message(message.from_user.id, 'СПИСОК МЕСТ:')
    bot.send_message(message.chat.id, data)
@bot.message_handler(commands=['reset'])
def reset_of_place(message):
    data.clear()
    bot.send_message(message.chat.id, 'ВМЕСТИЛИЩЕ ОЧИЩЕНО', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, timeout=10)
        except Exception as ex:
            print(ex.args)
            time.sleep(3)
