import telebot
from telebot import types
import sqlite3
from iot import iot_001
from iot import iot_005
from iot import iot_006
from iot import iot_132
from iot import iot_220
from database import sql
from database import db
import importlib


bot = telebot.TeleBot('7394659897:AAEGszaR4gSJ8tdP-9SPbM-n0Wim0cB4zIs')
#7394659897:AAEGszaR4gSJ8tdP-9SPbM-n0Wim0cB4zIs
#8131718795:AAGMPPS1v1dB4x4kWit2VCRI8eLz-98ilUE


@bot.message_handler(commands=['start'])
def start(message):
    mm = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("1 курс")
    button2 = types.KeyboardButton("2 курс")
    button3 = types.KeyboardButton("3 курс")
    button4 = types.KeyboardButton("4 курс")
    mm.add(button1,button2, button3, button4)
    bot.send_message(message.chat.id, "Привет, выбери свой курс", reply_markup=mm)
    
    sql.execute(f"SELECT chatid FROM userss WHERE chatid = '{message.chat.id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO userss VALUES(?,?,?)", (message.chat.id, message.from_user.username , 1))
        db.commit()
    else:
        for value in sql.execute("SELECT * FROM userss"):
            print(value)
    
@bot.message_handler(content_types=['text'])
def handler(message):
    if (message.text == "1 курс"):
        sql.execute(f"UPDATE userss SET level = 1 WHERE chatid = {message.chat.id}")
        db.commit()
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=mm)
    elif (message.text == "2 курс"):
        sql.execute(f"UPDATE userss SET level = 2 WHERE chatid = {message.chat.id}")
        db.commit()
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=mm)
    elif (message.text == "3 курс"):
        sql.execute(f"UPDATE userss SET level = 3 WHERE chatid = {message.chat.id}")
        db.commit()
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=mm)
    elif (message.text == "4 курс"):
        sql.execute(f"UPDATE userss SET level = 4 WHERE chatid = {message.chat.id}")
        db.commit()
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=mm)

    if message.text == "Посмотреть все ТБ для конкретного кабинета":
        mm = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton("Каб 233")
        button2 = types.KeyboardButton("Каб 252")
        button3 = types.KeyboardButton("Каб 318")
        button4 = types.KeyboardButton("Каб 108")
        button5 = types.KeyboardButton("Вернуться в главное меню")
        mm.add(button1, button2, button3, button4,button5)
        bot.send_message(message.chat.id, "Выберите кабинет", reply_markup=mm)

    if message.text == "Вернуться в главное меню":
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Возврат к меню", reply_markup=mm)

    if message.text == "Каб 233":
        bot.send_document(message.chat.id, open(r'220.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'132.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'001.pdf', 'rb'))
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Готово!", reply_markup=mm)
    
    if message.text == "Каб 252":
        bot.send_document(message.chat.id, open(r'220.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'132.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'001.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'003.pdf', 'rb'))
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Готово!", reply_markup=mm)
    
    if message.text == "Каб 318":
        bot.send_document(message.chat.id, open(r'005.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'006.pdf', 'rb'))
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Готово!", reply_markup=mm)
    
    if message.text == "Каб 108":
        bot.send_document(message.chat.id, open(r'220.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'132.pdf', 'rb'))
        bot.send_document(message.chat.id, open(r'003.pdf', 'rb'))
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть все ТБ для конкретного кабинета")
        button2 = types.KeyboardButton("Посмотреть конкретную ТБ")
        mm.add(button1, button2)
        bot.send_message(message.chat.id, "Готово!", reply_markup=mm)

    if message.text == "Посмотреть конкретную ТБ":
        mm = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton("ИОТ 001")
        button2 = types.KeyboardButton("ИОТ 005")
        button3 = types.KeyboardButton("ИОТ 006")
        button4 = types.KeyboardButton("ИОТ 132")
        button5 = types.KeyboardButton("ИОТ 220")
        button6 = types.KeyboardButton("Вернуться в главное меню")
        mm.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, "Выберите ТБ", reply_markup=mm)
  
    if message.text == "ИОТ 001":
        bot.send_message(message.chat.id, "Инструкция по охране труда и работе на персональном компьютере\n 1. Общие требования охраны труда (1.1 - 1.5)\n 2. Требования охраны труда перед началом работы (2.1 - 2.6) \n 3. Требования охраны труда во время работы (3.1 - 3.15)\n 4.Требования охраны труда в аварийных ситуациях (4.1 - 4.5) \n 5.Требования охраны труда по окончании работы. (5.1 - 5.2)\n Для вывода напишите например: '001 1 1' ")
    if message.text == "ИОТ 005":
        bot.send_message(message.chat.id, "Инструкция по охране труда для лиц, проводящих учебные и внеучебные занятия\n 1. Общие требования охраны труда (1.1 - 1.5)\n 2. Требования охраны труда перед началом работы (2.1 - 2.10) \n 3. Требования охраны труда во время работы (3.1 - 3.9)\n 4.Требования охраны труда в аварийных ситуациях (4.1 - 4.5) \n 5.Требования охраны труда по окончании работы. (5.1 - 5.7)\n Для вывода напишите например: '005 1 1' ")
    if message.text == "ИОТ 006":
        bot.send_message(message.chat.id, "Инструкция по охране труда для учебно-вспомогательного и учебно-производственного персонала\n 1. Общие требования охраны труда (1.1 - 1.6)\n 2. Требования охраны труда перед началом работы (2.1 - 2.4) \n 3. Требования охраны труда во время работы (3.1 - 3.11)\n 4.Требования охраны труда в аварийных ситуациях (4.1 - 4.6) \n 5.Требования охраны труда по окончании работы. (5.1 - 5.6)\n Для вывода напишите например: '006 1 1' ")
    if message.text == "ИОТ 132":
        bot.send_message(message.chat.id, "Инструкция по охране труда для обучающихся при выполнении лабораторных и практических работ в лабораториях с электроустановками до 1000 В\n 1. Общие требования охраны труда (1.1 - 1.12)\n 2. Требования охраны труда перед началом работы (2.1 - 2.5) \n 3. Требования охраны труда во время работы (3.1 - 3.10)\n 4.Требования охраны труда в аварийных ситуациях (4.1 - 4.5) \n 5.Требования охраны труда по окончании работы. (5.1 - 5.4)\n Для вывода напишите например: '132 1 1' ")
    if message.text == "ИОТ 220":
        bot.send_message(message.chat.id, "Инструкция по охране труда для обучающихся при работе на персональном компьютере \n 1. Общие требования охраны труда (1.1 - 1.6)\n 2. Требования охраны труда перед началом работы (2.1 - 2.6) \n 3. Требования охраны труда во время работы (3.1 - 3.13)\n 4.Требования охраны труда в аварийных ситуациях (4.1 - 4.4) \n 5.Требования охраны труда по окончании работы. (5.1 - 5.2)\n Для вывода напишите например: '220 1 1' ")
    if (message.text).split()[0]=='001':
        a,b,c = (message.text).split()
        bot.send_message(message.chat.id, iot_001[int(b)-1][int(c)-1])
    if (message.text).split()[0]=='005':
        a,b,c = (message.text).split()
        bot.send_message(message.chat.id, iot_005[int(b)-1][int(c)-1])
    if (message.text).split()[0]=='006':
        a,b,c = (message.text).split()
        bot.send_message(message.chat.id, iot_006[int(b)-1][int(c)-1])
    if (message.text).split()[0]=='132':
        a,b,c = (message.text).split()
        bot.send_message(message.chat.id, iot_132[int(b)-1][int(c)-1])
    if (message.text).split()[0]=='220':
        a,b,c = (message.text).split()
        bot.send_message(message.chat.id, iot_220[int(b)-1][int(c)-1])
  
bot.polling(none_stop=True)