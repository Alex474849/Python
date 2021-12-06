from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN




bot = Bot(TOKEN)
dp = Dispatcher(bot)

 
from bots.general import client as c

c.register_handlers_client(dp)





executor.start_polling(dp, skip_updates= True)