from aiogram import types, Dispatcher
from keyboards import get_main_kb
from aiogram.dispatcher.filters import Text


async def info_start(message: types.Message):
    await message.answer("PNX", reply_markup=get_main_kb())
    await message.delete()



def register_command_start(dp: Dispatcher):
    dp.register_message_handler(info_start, Text(equals="START", ignore_case = True))

