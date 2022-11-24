from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from keyboards import get_main_kb, get_which_instrument_kb, get_yes_no_kb
from media_db import sqlite




class FSMMedia(StatesGroup):
    which_instrument = State()
    send_video = State()


# Starting FSM

async def media_fsm(message: types.Message):  # MEDIA command, no state yet
    await message.delete()
    await FSMMedia.which_instrument.set()
    # Asking 1st question and giving specified keyboard with answers.
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
    async with state.proxy() as data:  # saving answer from the user into the state object of FSM
        data["instrument"] = message.text.lower()[1:-1]
        await FSMMedia.next()
    global list_of_id
    list_of_id = sqlite.get_videos_from_db(data["instrument"])
    # and sending first video of the chosen category
    await message.answer_video(next(sqlite.yield_id(list_of_id)), reply_markup=get_yes_no_kb())
    await message.answer("Wanna some more vids?")


async def send_video(message: types.Message, state=FSMContext):

    # Asking user if he wants one more video, and if yes, sending next video from db, until the answer is no
    # or if StopIteration happens...

    print("We have entered to send_video state")  # some debugging msg

    if message.text != "✔️YES✔️":
        await state.finish()    # exiting from FSM
        await message.answer("Ok, getting back to main menu", reply_markup=get_main_kb())
        return

    await message.answer_video(next(sqlite.yield_id(list_of_id)), reply_markup=get_yes_no_kb())
    # Setting FSM to present state again, and waiting if user answers no, or there will be no more content in database
    await state.set_state(FSMMedia.send_video)
    await message.answer("Wanna MOAR?", reply_markup=get_yes_no_kb())


def register_command_FSM(dp: Dispatcher):
    dp.register_message_handler(media_fsm, Text(
        equals="MEDIA", ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, Text(
        equals="🔇CANCEL🔇", ignore_case=True), state="*")  # here cancel button
    dp.register_message_handler(which_instrument, state=FSMMedia.which_instrument)
    # dp.register_message_handler(select_genre, state=FSMMedia.genre)
    # dp.register_message_handler(send_video, state=FSMMedia.send_media)
    dp.register_message_handler(send_video, state=FSMMedia.send_video)
