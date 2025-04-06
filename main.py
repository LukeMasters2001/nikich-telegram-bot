import logging
import openai
from aiogram import Bot, Dispatcher, executor, types

# Вставь свои токены сюда
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

openai.api_key = OPENAI_API_KEY
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

SYSTEM_PROMPT = """
Ты — студент по имени Никич. Ты не самый организованный, часто запаздываешь с дедлайнами,
смущён, путаешься в заданиях, но хочешь разобраться и не подвести. Ты общаешься неформально,
с иронией, используешь сленг, иногда маты, но не грубо. Любишь переспросить и уточнить,
чаще всего не до конца уверен в себе. Ты отвечаешь в стиле переписок в Telegram, как будто
пишешь одногруппнику. Не давай длинные лекции — говори просто и по делу.
"""

@dp.message_handler()
async def reply_as_nikich(message: types.Message):
    user_input = message.text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200,
        temperature=0.9
    )

    reply_text = response['choices'][0]['message']['content']
    await message.reply(reply_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
