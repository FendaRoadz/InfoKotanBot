from keyboards import get_info_keyboard
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


async def info_info(message: types.Message):
    await message.answer("Check out my social media:", reply_markup=get_info_keyboard())
    await message.delete()


def register_command_info(dp: Dispatcher):
    dp.register_message_handler(info_info, Text(equals="INFO", ignore_case = True))