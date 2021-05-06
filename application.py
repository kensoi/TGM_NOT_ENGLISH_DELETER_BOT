import string
import emoji

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'id:your_token_here'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

mylist = string.printable

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Hi! I delete a messages that isn't wroten in english letters!\nFollow the rules of the chat!"
        )
        
@dp.message_handler(commands=['test'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Why?"
        )


@dp.message_handler()
async def send_welcome(message: types.Message):
    if int(message.chat.id) == -1001279364623:
        for letter in emoji.demojize(message.text):
            if letter not in mylist:
                await bot.delete_message(message.chat.id, message.message_id)
                await bot.send_message(message.chat.id, "Follow the rules please")
                break
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
