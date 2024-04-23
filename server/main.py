from dotenv import load_dotenv 
import os
import base64
from requests import post, get
import json
from backEnd import *
import pickle
import time
import math


load_dotenv()

# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")

# def get_token():
#     auth_string = client_id + ":" + client_secret
#     auth_bytes = auth_string.encode("utf-8")
#     auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Authorization": "Basic " + auth_base64,
#         "Content-Type" : "application/x-www-form-urlencoded"
#     }
#     data = {"grant_type": "client_credentials"}
#     result = post(url, headers=headers, data=data)
#     json_result = json.loads(result.content)
#     token = json_result["access_token"]
#     return token

# def get_auth_header(token):
#     return{"Authorization": "Bearer " + token}



def load_song_list(filename):
    if not os.path.isfile(filename):
        return []
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except EOFError:  # If the file is empty, return an empty list
        return []


def main():
    playlist = []
    # token = get_token()
    playlist_filename = "playlist.txt"

    # print(get_album(token, "2uqYupMHANxnwgeiXTZXzd"))
    # playlist = load_playlist(playlist_filename)
    # make_playlist(token, playlist, playlist_filename)
    # songs = load_items_from_file("playlist.txt")
    # print(get_name(token, "5IgjP7X4th6nMNDh4akUHb"))

    counter = 0
    song_list = []
    filename = "songs.pkl"
    song_list = load_song_list(filename)

    with open("songs.pkl", "rb") as f:
        loaded_songs = pickle.load(f)

    counter = 0
    song_set = set()
    for song in loaded_songs:
        #  checks to see if has the artists component and if it is unique
         if hasattr(song, 'artists') and song.artists.strip():
                counter += 1
                # print(song.name, ''.join(song.artists), song.bpm, song.length, song.album, song.popularity)
                song_identifier = (song.name, song.artists)
                if song_identifier not in loaded_songs: 
                    insert_song_BackEnd(song, int(song.bpm)) 
                    song_set.add(song_identifier)
    

ascending_sort = use_quick_sort()
descending_sort = use_heap_sort()

def get_specific_Song(bpm):
    song_res = []
    for i in range(len(ascending_sort)):
        if (ascending_sort[i] in range(bpm, bpm + 1)):
            temp = bpms[ascending_sort[i]]
            for i in range(len(temp)):
                # print(temp[i].name, temp[i].artist, temp[i].bpm, temp[i].length, temp[i].album, temp[i].popularity)
                song_res.append(temp[i].name)
                song_res.append(temp[i].artist)
                song_res.append(temp[i].bpm)
                song_res.append(temp[i].length)
                song_res.append(temp[i].album)
                song_res.append(temp[i].popularity)
    return song_res

def get_specific_Songs(bpm):
    specific_songs = []
    if bpm in bpms:
        temp = bpms[bpm]
        for song in temp:
            if hasattr(song, 'artists'):
                song_data = {
                    'name': song.name,
                    'artist': song.artists,
                    'bpm': song.bpm,
                    'length': song.length,
                    'album': song.album,
                    'popularity': song.popularity
                }
                specific_songs.append(song_data)
                # print(song_data)
    else:
        print(f"No songs found for BPM: {bpm}")
    return specific_songs

# def get_range_Songs(start, end):
#     range_songs = []
#     for key in ascending_sort:
#         if start <= key <= end:
#             temp = bpms[key]
#             for song in temp:
#                 song_data = {
#                     'name': song.name,
#                     'artist': song.artist,
#                     'bpm': song.bpm,
#                     'length': song.length,
#                     'album': song.album,
#                     'popularity': song.popularity
#                 }
#                 range_songs.append(song_data)
#     print(range_songs)
#     return range_songs

# def get_range_Songs(start, end):
#     range_songs = []
#     for i in range(len(ascending_sort)):
#         if ascending_sort[i] in range(start, end):
#             temp = bpms[ascending_sort[i]]
#             for song in temp:
#                 song_data = {
#                     'name': song.name,
#                     'artist': song.artist,
#                     'bpm': song.bpm,
#                     'length': song.length,
#                     'album': song.album,
#                     'popularity': song.popularity
#                 }
#                 range_songs.append(song_data)
#     print(range_songs)
#     return range_songs

# good
# def get_range_Songs(start, end):
#     range_songs = []
#     for i in range(len(ascending_sort)):
#         if ascending_sort[i] in range(start, end):
#             temp = bpms[ascending_sort[i]]
#             for song in temp:
#                 song_data = {
#                     'name': song.name,
#                     'artist': song.artist,
#                     'bpm': song.bpm,
#                     'length': song.length,
#                     'album': song.album,
#                     'popularity': song.popularity
#                 }
#                 range_songs.append(song_data)

#     # Sort the range_songs list by BPM in ascending order
#     range_songs.sort(key=lambda x: x['bpm'])

#     return range_songs

def get_range_Songs(start, end):
    range_songs = []
    for i in range(len(ascending_sort)):
        if ascending_sort[i] in range(start, end):
            temp = bpms[ascending_sort[i]]
            for song in temp:
                if hasattr(song, 'artists'):
                    song_data = {
                        'name': song.name,
                        'artist': song.artists,
                        'bpm': song.bpm,
                        'length': song.length,
                        'album': song.album,
                        'popularity': song.popularity
                    }
                    range_songs.append(song_data)
                    
    # Sort the range_songs list by BPM in ascending order
    range_songs.sort(key=lambda x: x['bpm'])

    return range_songs



# def get_range_songs_descending(start, end):
#     range_songs_descending = []
#     for key in descending_sort:
#         if end >= key >= start:
#             temp = bpms[key]
#             for song in temp:
#                 song_data = {
#                     'name': song.name,
#                     'artist': song.artist,
#                     'bpm': song.bpm,
#                     'length': song.length,
#                     'album': song.album,
#                     'popularity': song.popularity
#                 }
#                 range_songs_descending.append(song_data)
#     return range_songs_descending


def get_range_songs_descending(start, end):
    range_songs_descending = []
    for key in descending_sort:
        if end >= key >= start:
            temp = bpms[key]
            for song in temp:
                if hasattr(song, 'artists'):
                    song_data = {
                        'name': song.name,
                        'artist': song.artists,
                        'bpm': song.bpm,
                        'length': song.length,
                        'album': song.album,
                        'popularity': song.popularity
                    }
                    range_songs_descending.append(song_data)

    # Sort the range_songs_descending list by BPM in descending order
    range_songs_descending.sort(key=lambda x: x['bpm'], reverse=True)

    return range_songs_descending



def get_min_Songs():
    temp = bpms[ascending_sort[0]]
    song_res = []
    for i in range(len(temp)):
        print(temp[i].name, temp[i].artist, temp[i].bpm, temp[i].length, temp[i].album, temp[i].popularity)
        song_res.append(temp[i].name)
        song_res.append(temp[i].artist)
        song_res.append(temp[i].bpm)
        song_res.append(temp[i].length)
        song_res.append(temp[i].album)
        song_res.append(temp[i].popularity)

    return song_res
def get_max_Songs():
    temp = bpms[descending_sort[0]]
    song_res = []
    for i in range(len(temp)):
        print(temp[i].name, temp[i].artist, temp[i].bpm, temp[i].length, temp[i].album, temp[i].popularity)
        song_res.append(temp[i].name)
        song_res.append(temp[i].artist)
        song_res.append(temp[i].bpm)
        song_res.append(temp[i].length)
        song_res.append(temp[i].album)
        song_res.append(temp[i].popularity)
    return song_res


if __name__ == "__main__":
    main()
    get_range_Songs(106,109)

    


