from aiogram.utils import executor
from aiogram import types
import logging
from bot_creation import dp
from handlers import info_hndlr, mediaFSM, command_hndlr 

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    print("Bot raised from ashes, dolboeb!")

command_hndlr.register_command_start(dp) 
info_hndlr.register_command_info(dp) 
mediaFSM.register_command_FSM(dp)

@dp.message_handler()
async def empty_handler(message: types.Message):
    await message.delete()
    await message.answer("Command unknown, please use commands from the provided keyboard!")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
