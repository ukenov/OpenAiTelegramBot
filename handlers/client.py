from aiogram import types, Dispatcher
from create_bot import dp
import openai

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply("Ask any question using command /Petuh")

#@dp.message_handler(commands=['Petuh'])
async def command_answer(message: types.Message):
    
    if message.text != '/Petuh':
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        await message.reply(response['choices'][0]['text'])
    else:
        await message.reply("Write you question after /Petuh")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_answer, commands=['Petuh'])