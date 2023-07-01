from bs4 import BeautifulSoup
import requests as r
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import os

USERNAME = '12177075489'
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"],


#Scrapping the musics
bilboard_url = "https://www.billboard.com/charts/hot-100/"

choosen_date = input("Which period do you want to see? (Type in YYYY-MM-DD): ")

bilboard_url = f"{bilboard_url}{choosen_date}"

response = r.get(bilboard_url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
title = soup.select("li ul li h3")
title_list = []
for t in title:
    title_list.append(t.getText().strip())

#Spotipy
spotipy = sp.Spotify(
    auth_manager=SpotifyOAuth(
        client_id= SPOTIPY_CLIENT_ID,
        client_secret= SPOTIPY_CLIENT_SECRET,
        redirect_uri= SPOTIPY_REDIRECT_URI,
        scope= "playlist-modify-private",
        show_dialog= True,
        cache_path= "token.txt",
        username= USERNAME, 
    )
)

user_id = spotipy.current_user()["id"]


#Searching songs, and getting spotfy links.
songs_uris = []
year = choosen_date.split("-")[0]
for i in title_list:
    result = spotipy.search(
        q=f"track:{i} year:{year}",
        type="track"
        )

    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        pass

#Create an playlist.
playlist = spotipy.user_playlist_create(
    user=USERNAME,
    name = f"Billboard 100({choosen_date.split('-')[2]}/{choosen_date.split('-')[1]}/{choosen_date.split('-')[0]})",
    public=False,
)

playlist_id = playlist["id"]

#Add musics.
spotipy.playlist_add_items(playlist_id=playlist_id, items=songs_uris)