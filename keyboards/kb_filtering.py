from media_db.video_commands import instruments

def filter_kb(keyword):
    if keyword in instruments.keys():
        return instruments[keyword]
