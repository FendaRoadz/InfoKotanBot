from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from keyboards import get_main_kb, get_which_instrument_kb, get_yes_no_kb
from media_db import sqlite


class FSMMedia(StatesGroup):
    which_instrument = State()  # state 0, answer which instrument
    send_video = State()

# Starting FSM 


async def media_fsm(message: types.Message):  # MEDIA command, no state yet
    await message.delete()
    await FSMMedia.which_instrument.set()
    await message.answer("Which instrument do you wanna see me playing?", reply_markup=get_which_instrument_kb())


async def cancel_handler(message: types.Message, state=FSMContext):  # CANCEL command
    await message.delete()
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Nothing to cancel", reply_markup=get_main_kb())
        return
    await state.finish()
    await message.answer("Cancelled\nPlease enter a command", reply_markup=get_main_kb())


async def which_instrument(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["instrument"] = message.text.lower()[1:-1]
    await FSMMedia.next()
    await message.answer(f"This is video of me playing whatever instrument you have chosen", reply_markup=get_yes_no_kb())
    await message.answer("Wanna some more vids?")


async def send_video(message: types.Message, state=FSMContext):
    print("We have entered to send_video state")
    if message.text != "✔️YES✔️":
        await state.finish()
        await message.answer("Ok, getting back to main menu", reply_markup=get_main_kb())
        i = 0
        return
    async with state.proxy() as data:
        await message.answer_video(next(sqlite.get_videos_from_db(data["instrument"])))
    await state.set_state(FSMMedia.send_video)
    await message.answer("Wanna MOAR?", reply_markup=get_yes_no_kb())

    # await message.answer_video(videos[0])

    # await message.answer("There is no more video yet... 😢")
    # await state.finish()

# async def send_video(message: types.Message, state = FSMContext):
#     await message.answer("Wanna MOAR?", reply_markup=get_yes_no_kb())
#     if message.text != "✔️YES✔️":


# async def send_video(message: types.Message, state: FSMContext): #SONG list in specific genre GENRE
#     async with state.proxy() as data:
#         data["song"] = message.text
#     await FSMMedia.next()
#     # send_video method calling here!
#     try:
#         await message.answer_video(sqlite.get_video(data["song"]), reply_markup=get_main_kb())
#         await message.answer("Here we go!")
#     except (BadRequest, TypeError):
#         await message.answer("There is no video yet 😢", reply_markup=get_main_kb())
#     await state.finish()

# async def select_genre(message: types.Message, state: FSMContext): # GENRE list
#     async with state.proxy() as data:
#         data["genre"] = message.text
#     question = "Which song do you like to hear?"
#     await FSMMedia.next()
#     if data["genre"] == "🎸METAL🎸":
#         await message.answer(question, reply_markup=get_metal_songs())
#     if data["genre"] == "🎸FUSION🎸":
#         await message.answer(question, reply_markup=get_fusion_songs())


def register_command_FSM(dp: Dispatcher):
    dp.register_message_handler(media_fsm, Text(
        equals="MEDIA", ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, Text(
        equals="🔇CANCEL🔇", ignore_case=True), state="*")  # here cancel button
    dp.register_message_handler(
        which_instrument, state=FSMMedia.which_instrument)

    # dp.register_message_handler(select_genre, state=FSMMedia.genre)
    # dp.register_message_handler(send_video, state=FSMMedia.send_media)
    dp.register_message_handler(send_video, state=FSMMedia.send_video)
