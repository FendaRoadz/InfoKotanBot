from aiogram import types, Dispatcher
from keyboards.kb_main import get_main_kb
from aiogram.dispatcher.filters import Text
from bot_creation import mail



async def info_start(message: types.Message):
    await message.answer("Please choose a command from the menu", reply_markup=get_main_kb())
    await message.delete()

async def email_send(message: types.Message):
    await message.answer(mail, reply_markup=get_main_kb())
    await message.delete()



def register_command_start(dp: Dispatcher):
    dp.register_message_handler(info_start, commands=["start"])
    dp.register_message_handler(email_send, commands=["mail"])




