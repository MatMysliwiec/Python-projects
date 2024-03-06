import eyed3


def modify_tag(file_path, title, artist, album, year, track_num, genre, album_art_path=None, additional_tags=None):
    audiofile = eyed3.load(file_path)

    audiofile.tag.title = title
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    audiofile.tag.year = year
    audiofile.tag.track_num = track_num
    audiofile.tag.genre = genre

    if album_art_path:
        with open(album_art_path, "rb") as image_file:
            album_art_data = image_file.read()
        audiofile.tag.images.set(3, album_art_data, "image/jpeg", u"Description")

    if additional_tags:
        for key, value in additional_tags.items():
            audiofile.tag.frame_set(key, value)

    audiofile.tag.save()


if __name__ == "__main__":
    file_path = ""
    title = ""
    artist = ""
    album = ""
    year = ""
    track_num = 1
    genre = ""
    album_art_path = ""
    additional_tags = {"TXXX": "Custom Tag"}

    modify_tag(file_path, title, artist, album, year, track_num, genre, album_art_path, additional_tags)
