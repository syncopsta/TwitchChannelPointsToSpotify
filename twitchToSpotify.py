import spotipy
from uuid import UUID
from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator
from spotipy.oauth2 import SpotifyOAuth
from twitchio.ext import pubsub

reward_name = "Add Song to Spotify Playlist"
streamer_name = "castcrafter"

spotify_client_id = ""
spotify_client_secret = ""
spotify_redirect_uri = "http://localhost:1337"
spotify_playlist = ""

twitch_client_id = ""
twitch_client_secret = ""


def callback_spotify(uuid: UUID, data: dict) -> None:
    for reward in Twitch.get_custom_reward(twitch, user_id)['data']:
        if reward_name in reward['title']:
            print("Playlist ID: "+reward['id'])
            playlist_reward_id = reward['id']

    if playlist_reward_id in data['data']['redemption']['reward']['id']:
        trackid = [data['data']['redemption']['user_input'].split("/track/")[1].split("?si")[0]]
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                    client_secret=spotify_client_secret,
                                                    redirect_uri=spotify_redirect_uri,
                                                    scope="playlist-modify-public"))

        sp.playlist_add_items(spotify_playlist, trackid)

twitch = Twitch(twitch_client_id, twitch_client_secret)

target_scope = [AuthScope.CHANNEL_READ_REDEMPTIONS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
token, refresh_token = auth.authenticate()
twitch.set_user_authentication(token, target_scope, refresh_token)

user_id = twitch.get_users(logins=streamer_name)['data'][0]['id']

pubsub = PubSub(twitch)
pubsub.start()
uuid = pubsub.listen_channel_points(user_id, callback_spotify)
input('press ENTER to close...')
pubsub.unlisten(uuid)
pubsub.stop()
