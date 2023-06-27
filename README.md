# Spotify Liked Songs Playlist Maker
 Takes your liked songs and creates a new playlist with them

# Set Up

- In the main.py file add the client_id, client_secret, redirect_uri and the username to the top of the file
    > You need to get this data from Spotify by creating a Spotify [app](https://developer.spotify.com/dashboard). Make sure to set REDIRECT_URI = "http://localhost:8888/callback" for testing
- Once the file is run you will log into Spotify on your browser and your Oauth will be logged
    > Once you log in, after a second a new playlist will be created titled "Liked Songs" 
