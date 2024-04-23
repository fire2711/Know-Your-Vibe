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
    
def save_song_list(filename, song_list):
    with open(filename, "wb") as f:
        pickle.dump(song_list, f)

def create_loaded(token, songs, song_list, filename):
    for i in range(1749, len(songs)):
        try:
            song = Song(get_name(token, songs[i]), get_artists(token, songs[i]), get_tempo(token, songs[i]), get_length(token,songs[i]), get_album(token,songs[i]), get_popularity(token,songs[i]))
            print(get_name(token, songs[i]))
            print(get_artists(token, songs[i]))
            print(get_tempo(token, songs[i]))
            print(get_length(token, songs[i]))
            print(get_album(token, songs[i]))
            print(get_popularity(token, songs[i]))
            if song not in song_list:
                song_list.append(song)
                counter += 1
    
        except Exception as e:
            print(f"An error occurred: {e}")
            save_song_list(filename, song_list)
        print(counter)
