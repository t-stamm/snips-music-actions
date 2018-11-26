import sys
import spotipy
import spotipy.util as util

class SpotifyController:

    def __init__(self):
        self.token = ""
        #self.token = 'AQBJdX-hFLsJ-BZXAFR6xa6C7OlE01PogTQid5wsnaKxtfVUmvnbLAg--8OwRezchrWVVIh6dS8BOFEvyv3LWiO_0p5hs8Vvpqblp39forKAqPTRi2dbNwso3zwQKVIf_0OLBiNx4WxAZ9y3JphFPbhOwF1SZ70SfkZloInnD3zYubsYilqqDL1ihpx9Yt47rp8986-uGARGfj-kHWTJNYkK7wdguFPx5X1KiWkzHW6HKY_1CslOltpqS32ThR2XD71ozL_FE_wOK2Bo08OidEl7B_UrvSlvyOpXR4Bvfd8uMyOmloQn5mBZ8cuRxj1T1JGLDGa-WA1dxwVRfdv-oR1KsIxlEbDJmebDr0fHozu8WNWO41z1Jy0y-9L0gvbcGQ'
        if not self.token or self.token == "":
            self.token = util.prompt_for_user_token('timo.stamm@gmx.de',
                'user-library-read playlist-read-private playlist-read-collaborative user-modify-playback-state user-read-currently-playing user-read-playback-state',
                client_id='06aa17352eba440db3aa332ca605ae14', 
                client_secret='f84b30beb6934037b44decd90c8a792b',
                redirect_uri='http://localhost/')

        self.sp = spotipy.Spotify(auth=self.token)
    
    def pause(self):
        self.sp.pause_playback()

    def next_track(self):
        self.sp.next_track()