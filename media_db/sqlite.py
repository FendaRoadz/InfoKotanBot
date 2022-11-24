import sqlite3
# from media_db import video_commands


def connect_to_db():
    global cur, base
    base = sqlite3.connect("kotan_media.db")
    cur = base.cursor()

    base.execute(
        "CREATE TABLE IF NOT EXISTS bass(filename PRIMARY KEY, file_id)")
    base.commit()
    base.execute(
        "CREATE TABLE IF NOT EXISTS keys(filename PRIMARY KEY, file_id)")
    base.commit()
    base.execute(
        "CREATE TABLE IF NOT EXISTS guitar(filename PRIMARY KEY, file_id)")
    base.commit()
    base.execute(
        "CREATE TABLE IF NOT EXISTS techno(filename PRIMARY KEY, file_id)")
    base.commit()
    if base:
        print("Sucsessfully connected to kotan_media.db")

# adding video to db (only admin)


async def insert_video(raw_data):
    async with raw_data.proxy() as data:
        category = data["category"]
        values = (data["name"], data["video"])
        cur.execute(f"INSERT INTO {category} VALUES (?, ?)", values)
        base.commit()

# code below doesn't work properly yet :(


def get_videos_from_db(category):
    return list((i[0] for i in cur.execute(f"SELECT file_id FROM {category}")))


def yield_id(list_of_id):
    for i in list_of_id:
        yield i
