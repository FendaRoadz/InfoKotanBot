from keyboards import get_main_kb
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from bot_creation import picture
#import mediafiles



async def tmp_placeholder(message: types.Message):
    await message.answer_photo(picture)
    await message.answer("This is a temporary placeholder,\n content will be available soon 💣", reply_markup= get_main_kb())

def register_tmp_placeholder(dp: Dispatcher):
    dp.register_message_handler(tmp_placeholder, Text(
        equals="COMING SOON", ignore_case=True), state=None)  