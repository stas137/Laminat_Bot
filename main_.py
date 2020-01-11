import os
import requests
import smtplib

import telebot
from telebot import types

#from settings import BOT_TOKEN, BIP_W, my_email, my_epass

global flag_oplat
flag_oplat = False

m2_10_Bip = '2700'
m2_25_Bip = '6300'
m2_50_Bip = '12000'

m2_10 = '11,10 м2 ['+ m2_10_Bip +' Bip]'
m2_25 = '26,64 м2 ['+ m2_25_Bip +' Bip]'
m2_50 = '51,06 м2 ['+ m2_50_Bip +' Bip]'
oplat = 'Я оплатил'


#print('Init '+ str(flag_oplat))

_start = '/start' 

bot = telebot.TeleBot(os.environ['BOT_TOKEN']);
#print(bot)

# обработка сообщений от пользователя 
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	
	global flag_oplat

	if message.text == _start:

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

		key_oplat = types.InlineKeyboardButton(text=oplat, callback_data='oplat')

		keyboard.add(key_oplat)

		# Показываем все кнопки сразу и пишем сообщение о выборе
		bot.send_message(message.from_user.id, text='Выберите необходимый объем ламината', reply_markup=keyboard)

	elif message.text == "/help":

		bot.send_message(message.from_user.id, "Для вывода меню напишите /start")

	elif flag_oplat == True:


		smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
		smtpObj.starttls()
		smtpObj.login(os.environ['my_email'], os.environ['my_epass'])
		smtpObj.sendmail(os.environ['my_email'], os.environ['my_email'], message.text)
		smtpObj.quit

		#print('Message from user ' + str(flag_oplat))
		flag_oplat = False
		#bot.send_message(message.from_user.id, "Для вывода помощи напишите /help")


	
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

	# Если нажали на одну из 12 кнопок — выводим гороскоп
	if call.data == "m2_10": 

		# Формируем ответ на выбор пользователя
		msg = 'Для покупки ' + m2_10 + ' отправьте сумму ' + m2_10_Bip + ' Bip на кошелек: ' + os.environ['BIP_W']

		# Отправляем текст в Телеграм
		bot.send_message(call.message.chat.id, msg)

	elif call.data == "m2_25": 

		# Формируем ответ на выбор пользователя
		msg = 'Для покупки ' + m2_25 + ' отправьте сумму ' + m2_25_Bip + ' Bip на кошелек: ' + os.environ['BIP_W']

		# Отправляем текст в Телеграм
		bot.send_message(call.message.chat.id, msg)

	elif call.data == "m2_50": 

		# Формируем ответ на выбор пользователя
		msg = 'Для покупки ' + m2_50 + ' отправьте сумму ' + m2_50_Bip + ' Bip на кошелек: ' + os.environ['BIP_W']

		# Отправляем текст в Телеграм
		bot.send_message(call.message.chat.id, msg)

	elif call.data == "oplat": 

		global flag_oplat

		flag_oplat = True
		#print('Cash ' + str(flag_oplat))
        # Формируем ответ на выбор пользователя
		msg = 'Введите ФИО, номер телефона, адрес куда отправить ламинат и номер кошелька с которого была произведена оплата (одной строкой)'

		# Отправляем текст в Телеграм
		bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)

