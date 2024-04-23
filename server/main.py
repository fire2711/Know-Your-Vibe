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

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

# returns tempo of song
def get_tempo(token, id):
    url = f"https://api.spotify.com/v1/audio-features/{id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tempo"]
    return json_result

# returns name of song
def get_name(token, id):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["name"]
    return json_result

# returns popularity of song
def get_popularity(token, id):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["popularity"]
    return json_result

# returns album
def get_album(token, id):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["album"]
    return json_result["name"]

# returns artists of songs
def get_artists(token, id):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["artists"]

    # returns a string
    artist_names = ", ".join(artist["name"] for artist in json_result)
    
    return artist_names

# returns length of song
def get_length(token, id):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["duration_ms"]

    # formats time into mm:ss
    duration_seconds = json_result / 1000
    minutes = int(duration_seconds // 60)
    seconds = int(duration_seconds % 60)
    time_formatted = f"{minutes:02d}:{seconds:02d}"
    
    return time_formatted

def search_track(token, name, offset):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={name}&type=track&offset={offset}"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if len(json_result) == 0:
        print("Error")
        return None

    return json_result[0]  # Return the first item in the list

def insert_song(song, playlist):
    # develops song database
    if song not in playlist:
        playlist.append(song) 

# save song database
def save_playlist(playlist, filename):
    with open(filename, 'a') as f:
        for song in playlist:
            f.write(song + '\n')

# loads song database
def load_playlist(filename):
    playlist = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                playlist.append(line.strip())
        print(f"Playlist loaded from {filename}")
        return playlist
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new playlist.")
        return []
    
def load_items_from_file(filename):
    items = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                item = line.strip()  
                items.append(item)  
        print(f"Items loaded from {filename}")
        return items  
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    
def make_playlist(token, playlist, name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # track_id = result["id"]\
    counter = 0

    # for each part of the alphabet add 900 songs
    for i in range (0, len(alphabet)):
        letter = alphabet[i]
        print(letter)
        for j in range(200):
            input = f"%25{letter}%25"
            try:
                result = search_track(token, input, j)
                if result:
                    print(result["name"] + " " + result["id"])
                    insert_song(result["id"], playlist)
                    counter += 1
            except Exception as e:
                print(f"An error occurred: {e}")
                save_playlist(playlist, name)

    for i in range(7, len(alphabet)):
        for j in range(len(alphabet)):
            letter1 = alphabet[i]
            letter2 = alphabet[j]
            print(f"{letter1} + {letter2}")
            input_combination = f"%25{letter1}{letter2}%25"
            for k in range(30):
                try:
                    result_combination = search_track(token, input_combination, k)
                    if result_combination:
                        print(result_combination["name"] + " " + result_combination["id"])
                        insert_song(result_combination["id"], playlist)
                        counter += 1
                except Exception as e:
                    print(f"An error occurred: {e}")
                    save_playlist(playlist, name)
    
    save_playlist(playlist, name)
    print(counter)

def load_song_list(filename):
    if not os.path.isfile(filename):
        return []
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except EOFError:  # If the file is empty, return an empty list
        return []

def save_song_list(filename, song_list):
    with open(filename, "wb") as f:
        pickle.dump(song_list, f)

def main():
    playlist = []
    token = get_token()
    playlist_filename = "playlist.txt"

    # print(get_album(token, "2uqYupMHANxnwgeiXTZXzd"))

    playlist = load_playlist(playlist_filename)

    # make_playlist(token, playlist, playlist_filename)

    songs = load_items_from_file("playlist.txt")

    # print(get_name(token, "5IgjP7X4th6nMNDh4akUHb"))
    counter = 0
    song_list = []
    filename = "songs.pkl"
    song_list = load_song_list(filename)
    # for i in range(1749, len(songs)):
    #     try:
    #         song = Song(get_name(token, songs[i]), get_artists(token, songs[i]), get_tempo(token, songs[i]), get_length(token,songs[i]), get_album(token,songs[i]), get_popularity(token,songs[i]))
    #         print(get_name(token, songs[i]))
    #         print(get_artists(token, songs[i]))
    #         print(get_tempo(token, songs[i]))
    #         print(get_length(token, songs[i]))
    #         print(get_album(token, songs[i]))
    #         print(get_popularity(token, songs[i]))
    #         if song not in song_list:
    #             song_list.append(song)
    #             counter += 1
    #
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         save_song_list(filename, song_list)
    #     print(counter)

    with open("songs.pkl", "rb") as f:
        loaded_songs = pickle.load(f)


    for song in loaded_songs:
        #print(song.name, song.artist, song.bpm, song.length, song.album, song.popularity)
        insert_song_BackEnd(song, int(song.bpm))


ascending_sort = use_quick_sort()
descending_sort = use_heap_sort()




def get_specific_Song(bpm):
    song_res = []
    for i in range(len(ascending_sort)):
        if (ascending_sort[i] in range(bpm, bpm + 1)):
            temp = bpms[ascending_sort[i]]
            for i in range(len(temp)):
                print(temp[i].name, temp[i].artist, temp[i].bpm, temp[i].length, temp[i].album, temp[i].popularity)
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
                print(song_data)
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

    


