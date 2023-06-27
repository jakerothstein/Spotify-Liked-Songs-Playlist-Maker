import math
import spotipy
import spotipy.util as util

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:8888/callback"  # Set this to "http://localhost:8888/callback" to run it locally
USERNAME = ""  # Put the username of the account registered with the API token

scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private user-library-read user-top-read'

token = util.prompt_for_user_token(
    username=USERNAME,
    scope=scope,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
)

sp = spotipy.Spotify(auth=token)

sp.user_playlist_create(user=USERNAME, name="Liked Songs", public=False)
playlist_id = sp.user_playlists(user=USERNAME)["items"][0]["id"]

song_list = []
tracks = sp.current_user_saved_tracks(limit=50, offset=0)
for i in range(math.ceil((int(tracks['total'])) / 50)):

    for item in tracks["items"]:
        song_list.append(item["track"]["external_urls"]["spotify"])
    sp.playlist_add_items(playlist_id=playlist_id, items=song_list)
    song_list = []

    tracks = sp.current_user_saved_tracks(limit=50, offset=((i + 1) * 50))
