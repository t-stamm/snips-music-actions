import sys
import spotipy
import spotipy.util as util

class SpotifyController:

    def __init__(self):
        self.token = ""
        if not self.token or self.token == "":
            #self.token = util.prompt_for_user_token('timo.stamm@gmx.de',
            #    'user-library-read playlist-read-private playlist-read-collaborative user-modify-playback-state user-read-currently-playing user-read-playback-state',
            #    client_id='06aa17352eba440db3aa332ca605ae14', 
            #    client_secret='f84b30beb6934037b44decd90c8a792b',
            #    redirect_uri='http://localhost/')

            print("Please open the following url edit this file content with the code parameter it returns:\r\n")
            print("https://accounts.spotify.com/authorize?scope=playlist-read-collaborative+playlist-read-private+user-library-read+user-modify-playback-state+user-read-currently-playing+user-read-playback-state&redirect_uri=http%3A%2F%2Flocalhost%2F&response_type=code&client_id=06aa17352eba440db3aa332ca605ae14\r\n")

            exit

        self.sp = spotipy.Spotify(auth=self.token)
    
    def pause(self):
        self.sp.pause_playback()

    def next_track(self):
        self.sp.next_track()