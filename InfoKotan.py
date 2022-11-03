from multiprocessing.managers import DictProxy
from aiogram.utils import executor
from aiogram import types
import logging
from bot_creation import dp
from handlers import info_hndlr, mediaFSM, command_hndlr, tmp_handler
from media_db import sqlite

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    print("Bot raised from ashes, dolboeb!")
    sqlite.connect_to_db()

command_hndlr.register_command_start(dp) 
info_hndlr.register_command_info(dp) 
mediaFSM.register_command_FSM(dp)
tmp_handler.register_tmp_placeholder(dp)

@dp.message_handler()
async def empty_handler(message: types.Message):
    await message.delete()
    await message.answer("Command unknown, please use commands from the provided keyboard!")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
