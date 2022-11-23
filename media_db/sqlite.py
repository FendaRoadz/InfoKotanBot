import sqlite3
# from media_db import video_commands

def connect_to_db():
    global cur, base
    base = sqlite3.connect("kotan_media.db")
    cur = base.cursor()

    base.execute("CREATE TABLE IF NOT EXISTS bass(filename PRIMARY KEY, file_id)")
    base.commit()
    base.execute("CREATE TABLE IF NOT EXISTS keys(filename PRIMARY KEY, file_id)")
    base.commit()
    base.execute("CREATE TABLE IF NOT EXISTS guitar(filename PRIMARY KEY, file_id)")
    base.commit()
    base.execute("CREATE TABLE IF NOT EXISTS techno(filename PRIMARY KEY, file_id)")
    base.commit()
    if base:
        print ("Sucsessfully connected to kotan_media.db")

# adding video to db
async def insert_video(raw_data):
    async with raw_data.proxy() as data:
        category = data["category"]
        values = (data["name"], data["video"])
        cur.execute(f"INSERT INTO {category} VALUES (?, ?)", values)
        base.commit()


# sending video to client
# async def get_video(name, category):
#         for key in video_commands.video_dict:
#             if key == name:
#                 return cur.execute(f"SELECT file_id FROM {category} WHERE filename == ?", (video_commands.video_dict[key],)).fetchone()[0]




def get_videos_from_db(category):
    id_list = list((i[0] for i in cur.execute(f"SELECT file_id FROM {category}")))
    for i in id_list:
        yield i

 
    
 
# connect_to_db()
# print (get_video("🤘MESHUGGAH🤘"))
# print (video_dict)

# make_json()

# print (get_videos_from_db("bass"))