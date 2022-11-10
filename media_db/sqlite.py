import sqlite3
from media_db import video_commands

def connect_to_db():
    global cur, base
    base = sqlite3.connect("kotan_media.db")
    cur = base.cursor()

    base.execute("CREATE TABLE IF NOT EXISTS video(filename PRIMARY KEY, file_id)")
    base.commit()
    if base:
        print ("Sucsessfully connected to kotan_media.db")

# adding video to db
async def insert_video(raw_data):
    async with raw_data.proxy() as data:
        cur.execute("INSERT INTO video VALUES (?, ?)", tuple(data.values()))
        base.commit()


# sending video to client
def get_video(name):
        for key in video_commands.video_dict:
            if key == name:
                return cur.execute("SELECT file_id FROM video WHERE filename == ?", (video_commands.video_dict[key],)).fetchone()[0]


# connect_to_db()
# print (get_video("🤘MESHUGGAH🤘"))
# print (video_dict)

# make_json()