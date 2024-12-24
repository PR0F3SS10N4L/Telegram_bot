import telebot
from telebot import types
import sqlite3

db = sqlite3.connect('users.db', check_same_thread = False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    chatid TEXT,
    username TEXT,
    lvl INT
)""") 
db.commit()


bot = telebot.TeleBot('8131718795:AAGMPPS1v1dB4x4kWit2VCRI8eLz-98ilUE')

mm = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button1 = types.KeyboardButton("Каб 233")
button2 = types.KeyboardButton("Каб 252")
button3 = types.KeyboardButton("Каб 318")
button4 = types.KeyboardButton("Каб 108")
button5 = types.KeyboardButton("Посмотреть уровень допуска")
button6 = types.KeyboardButton("Поменять уровень допуска на 1")
button7 = types.KeyboardButton("Поменять уровень допуска на 2")
button8 = types.KeyboardButton("Поменять уровень допуска на 3")
mm.add(button1,button2, button3, button4, button5, button6, button7, button8)

@bot.message_handler(commands=['start'])
def start(message):
    sql.execute(f"SELECT chatid FROM users WHERE chatid = '{message.chat.id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?,?,?)", (message.chat.id, message.from_user.username, 1))
        db.commit()
    '''
    else:
        for value in sql.execute("SELECT * FROM users"):
            print(value)'''
    bot.send_message(message.chat.id, "Привет, выбери кабинет в котором ты выполняешь работу", reply_markup=mm)
    


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "123":
        sql.execute('SELECT * FROM users')
        users = sql.fetchall()
        # Выводим результаты
        for user in users:
            print(user)



    
    if message.text == "Посмотреть уровень допуска":
        for value in sql.execute(f"SELECT lvl FROM users WHERE chatid = ({message.chat.id})"):
            bot.send_message(message.chat.id, f"Твой уровень допуска: {value[0]}", parse_mode='html')
            db.commit()
    if message.text == "Поменять уровень допуска на 1":
        sql.execute(f"UPDATE users SET level = 1 WHERE chatid = {message.chat.id}")
        db.commit()
        bot.send_message(message.chat.id, "Готово")
    if message.text == "Поменять уровень допуска на 2":
        sql.execute(f"UPDATE users SET level = 2 WHERE chatid = {message.chat.id}")
        db.commit()
        bot.send_message(message.chat.id, "Готово")
    if message.text == "Поменять уровень допуска на 3":
        sql.execute(f"UPDATE users SET level = 3 WHERE chatid = {message.chat.id}")
        db.commit()
        bot.send_message(message.chat.id, "Готово")

    if message.text == "Каб 233":
        sql.execute(f"SELECT level FROM users WHERE chatid = '{message.chat.id}'")
        if sql.fetchone() == 1:
            bot.send_message(message.chat.id, "Держи!")
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\220.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\132.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\001.pdf', 'rb'))
        db.commit()
  
    if message.text == "Каб 252":
        sql.execute(f"SELECT level FROM users WHERE chatid = '{message.chat.id}'")
        if sql.fetchone() == 2:
            bot.send_message(message.chat.id, "Держи!")
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\220.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\132.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\001.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\003.pdf', 'rb'))
        else:
            bot.send_message(message.chat.id, "Недостаточный уровень допуска")
        db.commit()

    if message.text == "Каб 318": 
        sql.execute(f"SELECT level FROM users WHERE chatid = '{message.chat.id}'")
        if sql.fetchone() == 3:
            bot.send_message(message.chat.id, "Держи!")
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\005.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\006.pdf', 'rb'))
        else:
            bot.send_message(message.chat.id, "Недостаточный уровень допуска")
        db.commit()

    if message.text == "Каб 108":
        sql.execute(f"SELECT level FROM users WHERE chatid = '{message.chat.id}'")
        if sql.fetchone() == 3:
            bot.send_message(message.chat.id, "Держи!")
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\220.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\132.pdf', 'rb'))
            bot.send_document(message.chat.id, open(r'C:\Users\Миша\Desktop\Проги\TG_BOT\003.pdf', 'rb'))
        else:
            bot.send_message(message.chat.id, "Недостаточный уровень допуска")
        db.commit()

        
bot.polling(none_stop=True)





    