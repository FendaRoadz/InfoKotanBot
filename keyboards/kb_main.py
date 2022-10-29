from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

butt_cancel = KeyboardButton("🔇CANCEL🔇")

def get_main_kb():
    butt_start = KeyboardButton("START")
    butt_info = KeyboardButton("INFO")
    butt_media = KeyboardButton("MEDIA")
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    main_kb.add(butt_start).add(butt_media).add(butt_info)
    return main_kb

def get_genre_kb():

    butt_metal = KeyboardButton("🎸METAL🎸")
    butt_fusion = KeyboardButton("🎸FUSION🎸")
    genre_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    genre_kb.add(butt_metal).add(butt_fusion).add(butt_cancel)
    return genre_kb

def get_metal_songs():
    butt_meshuggah = ("🤘MESHUGGAH 🤘")
    butt_matheria = ("🤘MATHERIA🤘")
    metal_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    metal_kb.add(butt_meshuggah).add(butt_matheria).add(butt_cancel)
    return metal_kb

def get_fusion_songs():

    butt_braziluba = ("🎷BRAZILUBA🎷")
    butt_de_rena = ("🎷DeRena🎷")
    fusion_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    fusion_kb.add(butt_braziluba).add(butt_de_rena).add(butt_cancel)
    return fusion_kb



