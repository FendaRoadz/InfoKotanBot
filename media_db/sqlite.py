import sqlite3
import json


video_dict = {"🤘MESHUGGAH🤘": "MESHUGGAH", "🤘MATHERIA🤘": "MATHERIA", "🎷BRAZILUBA🎷":"BRAZILUBA", \
                "🎷DeRena🎷": "DERENA"}
def make_json():
    with open("video_dict.json", "a") as f: 
        json.dump(video_dict, f)


def connect_to_db():
    global cur, base
    base = sqlite3.connect("kotan_media.db")
    cur = base.cursor()

    base.execute("CREATE TABLE IF NOT EXISTS media(filename PRIMARY KEY, file_id)")
    base.commit()

    cur.execute("INSERT INTO media VALUES (?,?)", ("MESHUGGAH", "BAACAgIAAxkBAAEZlB9jYjeT2ojEAaJoSBsm_66KcahSswACYCAAAozZEEsG-auitDfjOSoE"))


def get_video(name):
    for key in video_dict:
        if key == name:
            return cur.execute("SELECT file_id FROM media WHERE filename == ?", (video_dict[key],)).fetchone()[0]


# connect_to_db()
# print (get_video("🤘MESHUGGAH🤘"))
# print (video_dict)

make_json()