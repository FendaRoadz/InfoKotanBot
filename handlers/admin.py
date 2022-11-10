from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from media_db import sqlite

class FSMAdmin(StatesGroup):
    name = State()
    video = State()

async def admin_fsm_start(message: types.Message, state=None):
    await FSMAdmin.name.set()
    # await message.delete()
    await message.answer("Enter the name of the video")

async def admin_enter_name(message: types.Message, state=FSMContext):
    await message.delete() 
    async with state.proxy() as data:
        data["name"] = message.text.lower()
    await FSMAdmin.next()
    await message.answer("Upload video")

async def admin_upload_video(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["video"] = message.video.file_id
    async with state.proxy() as data:
        await message.reply("Video uploaded!")
        await sqlite.insert_video(state)
    
    await state.finish()


def register_command_admin(dp: Dispatcher):
    dp.register_message_handler(admin_fsm_start, commands=["load_video"], state=None)
    dp.register_message_handler(admin_enter_name, state=FSMAdmin.name)
    dp.register_message_handler(admin_upload_video, content_types=["video"], state=FSMAdmin.video)

