import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(album):
    for album in album:
        for song in os.listdir(album[0]):
            yield song


album_list = find_albums("music", "Black*")
song_list = find_songs(album_list)

for s in song_list:
    print(s)

# for a in album_list:
#     print(a)
