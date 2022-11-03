from keyboards import get_main_kb
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import mediafiles

async def tmp_placeholder(message: types.Message):
    await message.answer_photo("https://sun9-81.userapi.com/impf/c851228/v851228330/4854d/FsZH0NwKErE.jpg?size=720x960&quality=96&sign=69896d5555eeefb148e6f8645785251d&type=album")
    await message.answer("This is a temporary placeholder,\n content will be available soon 💣", reply_markup= get_main_kb())

def register_tmp_placeholder(dp: Dispatcher):
    dp.register_message_handler(tmp_placeholder, Text(
        equals="COMING SOON", ignore_case=True), state=None)  