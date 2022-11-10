from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from keyboards import get_main_kb, get_genre_kb, get_metal_songs, get_fusion_songs
from keyboards.kb_main import get_main_kb
from media_db import sqlite
from aiogram.utils.exceptions import BadRequest


class FSMMedia(StatesGroup):
    genre = State()  # state 0, answer: what genre.
    song = State()  # state 1, answer which song
    send_media = State()  # state 2, final, answer - send actual media

# Starting FSM


async def media_fsm(message: types.Message):
    await message.delete()
    await FSMMedia.genre.set()
    # here buttons with genre needs to be
    await message.answer("Select genre", reply_markup=get_genre_kb())


async def cancel_handler(message: types.Message, state=FSMContext):
    await message.delete()
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Nothing to cancel", reply_markup=get_main_kb())
        return
    await state.finish()
    await message.answer("Cancelled\nPlease enter a command", reply_markup=get_main_kb())

async def select_genre(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["genre"] = message.text
    question = "Which song do you like to hear?"
    await FSMMedia.next()
    if data["genre"] == "🎸METAL🎸":
        await message.answer(question, reply_markup=get_metal_songs())
    if data["genre"] == "🎸FUSION🎸":
        await message.answer(question, reply_markup=get_fusion_songs())

async def select_song(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["song"] = message.text
    await FSMMedia.next()
    # send video method calling here!
    try:
        await message.answer_video(sqlite.get_video(data["song"]), reply_markup=get_main_kb())
        await message.answer("Here we go!")
    except (BadRequest, TypeError):
        await message.answer("There is no video yet 😢", reply_markup=get_main_kb())
    await state.finish()


def register_command_FSM(dp: Dispatcher):
    dp.register_message_handler(media_fsm, Text(
        equals="MEDIA", ignore_case=True), state=None)  
    dp.register_message_handler(cancel_handler, Text(
        equals="🔇CANCEL🔇", ignore_case=True), state="*") # here cancel button
    dp.register_message_handler(select_genre, state=FSMMedia.genre)
    dp.register_message_handler(select_song, state=FSMMedia.song)
