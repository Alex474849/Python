from aiogram import types, Dispatcher
from general.bot_telegram import dp, bot





#@dp.message_handler(commands= ['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Приятного аппетита')

#@dp.message_handler(commands= ['working_time'])
async def pizza_open(message :types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт - с 9 00 до 22 00, Сб-Вс - Выходной')


#@dp.message_handler(commands= ['location'])
async def location(message :types.Message):
    await bot.send_message(message.from_user.id, 'Проспект Мира 13')

#@dp.message_handler(commands= ['Menu'])
#async def menu(message : types.Message):


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands= ['start', 'help'])
    dp.register_message_handler(pizza_open, commands= ['working_time'])
    dp.register_message_handler(location, commands= ['location'])