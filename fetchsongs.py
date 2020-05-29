"""
Module to start

"""

from googleapiclient.discovery import build
from pprint import pprint
import json
import datetime

DEVELOPER_KEY = "AIzaSyBx6KooXq71ibITeIs5qG0u0nXwWy72RWY"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
MAXCOUNT=1

ARTISTS = {
    "KK",
    "Neha Kakkar",
    "Tanishk Baghchi",
    "Badhshah",
    "Mika Singh",
    "Arijit Singh",
    "Armaan Malik",
    "Mohit Chauhan",
    "Atif Aslam",
    "Sunidhi Chauhan",
    "Shreya Ghoshal",
    "Yo Yo Honey Singh",
    "Lata Mangeshkar",
    "Astha Gill",
    "Sonu Nigam",
    "Udit Narayan",
    "Kumar Sanu",
    "Shaan",
    "Rahat Fateh Ali Khan",
    "A.R Rahman",
    "Ankit Tiwari",
    "Sukhwinder Singh",
    "Pritam",
    "Himesh Reshammiya",
    "Abhijit Bhattacharya",
    "Kanika Kapoor",
    "Ayushman Khurrana",
    "Vishal Dadlani",
    "kailash Kher",
    "Adnan Sami",
    "Dhanush",
}

# load the json filter it and use it if lag us
CHANNELS = json.load(open("currchannels.json", "r")) 


CHANNELS = {
    k: 0
    for k, v in CHANNELS.items()
    if v >= 4
}

# CHANNELS = {
#     "T-Series": 0,
#     "Zee Music Company": 0,
#     "Sony Music India": 0,
#     "YRF": 0,
#     "Tips Official": 0,
#     "Shemaroo Filmi Gaane": 0,
#     "SonyMusicIndiaVEVO": 0,
#     "Venus": 0,
#     "Red Chillies Entertainment": 0,
# # }
# result = {}
# try:
#     # define the service
#     youtube = build(
#         YOUTUBE_API_SERVICE_NAME,
#         YOUTUBE_API_VERSION,
#         developerKey=DEVELOPER_KEY
#     )

#     total = 0

#     # make a serach and print the contents
#     for artist in ARTISTS:
#         response = youtube.search().list(
#             q=f"{artist} songs",
#             part='id,snippet',
#             maxResults=MAXCOUNT,
#             order='viewCount',
#             type='video'
#         ).execute()
#         result[artist] = response.get('items', [])
#         for song in result[artist]:
#             channel = song["snippet"]["channelTitle"]
#             CHANNELS[channel] = CHANNELS.get(channel, 0) + 1
#         result[artist] = list(filter(
#             lambda x: x["snippet"]["channelTitle"] in CHANNELS,
#             result[artist]
#         ))
#         total+=len(result[artist])


#     result = {
#         "time": datetime.datetime.now(),
#         "songs": result
#     }

#     json.dump(CHANNELS, open("currchannels.json", "w"), indent=4, default=str)
#     json.dump(result, open("currsongs.json", "w"), indent=4, default=str)

#     print(f"Total {total} songs retrieved from {len(CHANNELS)} channels")

# except Exception as e:
#     print(f"Error {e} occured. Shifting to existing data")

result = json.load(open("currsongs.json", "r"))
"""
Download these videoas and store them in mp3
"""
from pytube import YouTube

for artist, songs in result["songs"].items():
    for song in songs:
        url = f"htts:/www.youtube.com/watch?v={song['id']['videoId']}"
        y = YouTube(url)
        print(f"Downloading song {song['snippet']['title']} of artis {artist}")
        t = y.streams.filter(only_audio=True)
        t[0].download(output_path="./songs/")
