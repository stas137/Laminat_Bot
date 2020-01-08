import sys
import requests

import datetime
from time import sleep

import telebot
from telebot import types
	
import random

"""

answer = {}
answer['chat_id'] = get_chat_id(last_update(get_updates_json(BASE_URL)))
answer['text'] = 'Добрый день'
r = requests.post(f'{BASE_URL}sendMessage', data=answer)
"""

print(sys.platform)
print(2 ** 10)
x = 'Spam!'
print(x*8)


BOT_TOKEN = '1035878512:AAEZMLARv0F_0xcsabz4RpiEISJXBpCAObI'
print(BOT_TOKEN)

BASE_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'
print(BASE_URL)


# обновления за последние 24 часа
def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None} # offset помечаем просмотренные обновления
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()
	#r = requests.get(f'{BASE_URL}getUpdates')


# последнее обновление
def get_last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

	# сокращенная форма
	#print(r.json()['result'][-1])


# получить id чата
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id


# отправка сообщения
def send_mess(url, chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

#send_mess(BASE_URL, get_chat_id(last_update(get_updates_json(BASE_URL))), 'Добрый')
"""

# получить информацию о боте
r = requests.get(f'{BASE_URL}getMe')
print(r)
print(r.json())

# получить обновления за 24 часа
response = requests.get(BASE_URL + 'getUpdates')
print(response.json())


def main():  
    update_id = get_last_update(get_updates_json(BASE_URL))['update_id']
    while True:
        if update_id == get_last_update(get_updates_json(BASE_URL))['update_id']:
           send_mess(BASE_URL, get_chat_id(get_last_update(get_updates_json(BASE_URL))), 'test')
           update_id += 1
        sleep(1)       
"""
m2_10_Bip = '2600'
m2_25_Bip = '6240'
m2_50_Bip = '11960'

m2_10 = '11,10 м2 ['+ m2_10_Bip +' Bip]'
m2_25 = '26,64 м2 ['+ m2_25_Bip +' Bip]'
m2_50 = '51,06 м2 ['+ m2_50_Bip +' Bip]'

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.offset = None

        self.method_getUpdates = 'getUpdates'
        self.method_sendMessage = 'sendMessage'
        self.method_getUpdates = 'getUpdates'

        self.m2_10 = m2_10
        self.m2_25 = m2_25
        self.m2_50 = m2_50

    def get_updates(self, timeout=300):
        #method = 'getUpdates'
        params = {'timeout': timeout, 'offset': self.offset}
        resp = requests.get(self.api_url + self.method_getUpdates, params)
        result_json = resp.json()['result']
        print(result_json)
        print('')
        return result_json

    def send_message(self, chat_id, text, reply_markup=None):
        params = {'chat_id': chat_id, 'text': text, 'reply_markup': reply_markup}
        #method = 'sendMessage'
        resp = requests.post(self.api_url + self.method_sendMessage, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update    


laminat_bot = BotHandler(BOT_TOKEN)  
_start = '/start' 
now = datetime.datetime.now()

bot = telebot.TeleBot(BOT_TOKEN);
print(bot)

# Заготовки для трёх предложений

first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]

 
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

	if message.text == "/start":

		bot.send_message(message.from_user.id, "Здесь вы можете обменять BIP на ламинат Кроношпан Дуб Гренландский 8мм 32класс. Работает только в России!")

		# Готовим кнопки
		keyboard = types.InlineKeyboardMarkup()

		# По очереди готовим текст и обработчик для каждого объема ламината

		key_m2_10 = types.InlineKeyboardButton(text=m2_10, callback_data='m2_10')

		# И добавляем кнопку на экран

		keyboard.add(key_m2_10)

		key_m2_25 = types.InlineKeyboardButton(text=m2_25, callback_data='m2_25')

		keyboard.add(key_m2_25)

		key_m2_50 = types.InlineKeyboardButton(text=m2_50, callback_data='m2_50')

		keyboard.add(key_m2_50)


		# Показываем все кнопки сразу и пишем сообщение о выборе

		bot.send_message(message.from_user.id, text='Выберите необходимый объем ламината', reply_markup=keyboard)

	elif message.text == "/help":

		bot.send_message(message.from_user.id, "Для вывода меню напишите /start")

	else:

		bot.send_message(message.from_user.id, "Для вывода помощи напишите /help")



	



	
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "m2_10": 

        # Формируем ответ на выбор пользователя

        msg = 'Для покупки ' + m2_10 + ' отправьте сумму ' + m2_10_Bip + ' Bip на кошелек: Mx072fda1d4817bc5263eafb50df8824d48033f83f'

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)

    elif call.data == "m2_25": 

        # Формируем ответ на выбор пользователя

        msg = 'Для покупки ' + m2_25 + ' отправьте сумму ' + m2_25_Bip + ' Bip на кошелек: Mx072fda1d4817bc5263eafb50df8824d48033f83f'

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)

    elif call.data == "m2_50": 

        # Формируем ответ на выбор пользователя

        msg = 'Для покупки ' + m2_50 + ' отправьте сумму ' + m2_50_Bip + ' Bip на кошелек: Mx072fda1d4817bc5263eafb50df8824d48033f83f'

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)

"""
def main():  


	new_offset = None
	today = now.day
	hour = now.hour

	laminat_bot.offset = new_offset

	last_update = laminat_bot.get_last_update()

	last_update_id = last_update['update_id']

	print(last_update_id)
	print('')

	last_chat_text = last_update['message']['text']
	last_chat_id = last_update['message']['chat']['id']
	last_chat_name = last_update['message']['chat']['first_name']

	if last_chat_text.lower() == _start and today == now.day and 6 <= hour < 12:
		laminat_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
		laminat_bot.send_message(last_chat_id, 'Здесь вы можете обменять BIP на ламинат Кроношпан Дуб Гренландский 8мм 32класс')
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_10)
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_25)
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_50)
	    
	    #today += 1

	elif last_chat_text.lower() == _start and today == now.day and 12 <= hour < 17:
		laminat_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
		laminat_bot.send_message(last_chat_id, 'Здесь вы можете обменять BIP на ламинат Кроношпан Дуб Гренландский 8мм 32класс')
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_10)
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_25)
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_50)
	
	    #today += 1

	elif last_chat_text.lower() == _start and today == now.day and 17 <= hour < 23:
		laminat_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
		laminat_bot.send_message(last_chat_id, 'Здесь вы можете обменять BIP на ламинат Кроношпан Дуб Гренландский 8мм 32класс')
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_10)
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_25)
		laminat_bot.send_message(last_chat_id, laminat_bot.m2_50)

		keyboard = types.InlineKeyboardMarkup()
		callback_button = types.InlineKeyboardButton(text="Создать пароль", callback_data="start")
		keyboard.add(callback_button)
		laminat_bot.send_message(last_chat_id, 'Привет! Я бот который поможет тебе придумать пароли\nДля начала нажми на кнопку ниже', keyboard)

	
	    #today += 1

	new_offset = last_update_id + 1
	laminat_bot.offset = new_offset

	while True:

		last_update = laminat_bot.get_last_update()

		last_update_id = last_update['update_id']
		last_chat_text = last_update['message']['text']
		last_chat_id = last_update['message']['chat']['id']
		last_chat_name = last_update['message']['chat']['first_name']

		print(last_update_id)
		print('')

		if last_chat_text.lower() != _start:
			laminat_bot.send_message(last_chat_id, 'Для вызова меню напишите /start')
		
		else:
			laminat_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
			laminat_bot.send_message(last_chat_id, 'Здесь вы можете обменять BIP на ламинат Кроношпан Дуб Гренландский 8мм 32класс')
			laminat_bot.send_message(last_chat_id, laminat_bot.m2_10)
			laminat_bot.send_message(last_chat_id, laminat_bot.m2_25)
			laminat_bot.send_message(last_chat_id, laminat_bot.m2_50)

		new_offset = last_update_id + 1
		laminat_bot.offset = new_offset










if __name__ == '__main__':  

    try:
        main()
    except KeyboardInterrupt:
        exit()
"""