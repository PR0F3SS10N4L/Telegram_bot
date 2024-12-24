import re
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from g4f.client import Client
from aiogram.fsm.storage.memory import MemoryStorage
import logging
import sqlite3



API_TOKEN = '8131718795:AAGMPPS1v1dB4x4kWit2VCRI8eLz-98ilUE'  

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

client = Client()

conversation_history = {}

#DISCORD_INVITE_PATTERN = re.compile(r'https://discord\.com/invite/q55gsH8z5F', re.IGNORECASE)

def clear_chat_history(user_id):
    conversation_history[user_id] = []

#def contains_prohibited_link(text):
#    return bool(DISCORD_INVITE_PATTERN.search(text))

@dp.message(Command("start"))
async def send_welcome(message: Message):
    user_id = message.from_user.id
    clear_chat_history(user_id)  
    await message.answer("Привет! Напиши мне что-нибудь.")

@dp.message(Command("clear"))
async def clear_history(message: Message):
    user_id = message.from_user.id
    clear_chat_history(user_id)  
    await message.answer("История чата очищена.")

@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    user_input = message.text

    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history[user_id],  
            max_tokens=500
        )

        gpt_response = response.choices[0].message.content

        if contains_prohibited_link(gpt_response):
            await message.answer("Произошла ошибка: ответ содержит запрещенную ссылку.")
        else:
            conversation_history[user_id].append({"role": "assistant", "content": gpt_response})
            await message.answer(gpt_response)
    
    except Exception as e:
        await message.answer(f"Произошла ошибка при обработке сообщения: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
