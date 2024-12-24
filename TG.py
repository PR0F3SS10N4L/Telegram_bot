#pip install python-telegram-bot sqlite3
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3
# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# Подключение к базе данных
conn = sqlite3.connect('safety_bot.db')
cursor = conn.cursor()
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    # Проверка и регистрация пользователя
    cursor.execute("INSERT OR IGNORE INTO Users (id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    update.message.reply_text('Добро пожаловать! Используйте команду /safety для получения информации о технике безопасности.')
def safety(update: Update, context: CallbackContext) -> None:
    lab_name = ' '.join(context.args)
    cursor.execute("SELECT safety_info FROM SafetyProcedures WHERE lab_name = ?", (lab_name,))
    result = cursor.fetchone()
    if result:
        update.message.reply_text(result[0])
    else:
        update.message.reply_text('Информация о технике безопасности не найдена.')
def main() -> None:
    updater = Updater("8131718795:AAGMPPS1v1dB4x4kWit2VCRI8eLz-98ilUE")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("safety", safety))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()