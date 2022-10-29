from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

def get_info_keyboard():
    butt_insta = InlineKeyboardButton(text = "Instagram", url = "instagram.com/kotanmusic")
    butt_twitter = InlineKeyboardButton(text = "Twitter", url = "twitter.com/fendaroadz")
    info_inline_keyboard = InlineKeyboardMarkup(row_width=3)
    info_inline_keyboard.row(butt_insta, butt_twitter)
    return info_inline_keyboard