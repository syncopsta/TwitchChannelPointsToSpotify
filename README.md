# TwitchChannelPointsToSpotify
This is a python script to create a community playlist with channel points rewards.

# Python modules
  * spotipy
  * twitchAPI
  * twitchio

# Requirements
  * A twitch application
    - create it on https://dev.twitch.tv/console
      - The name is not relevant, use a meaningful name
      - OAuth Redirect URLs: http://localhost:17563
      - Kategorie: Application Integration
      - Get your Client ID und Client Secret
      - Add them to the script

- Eine Spotify Anwendung
  - create it on https://developer.spotify.com/dashboard/applications
    - The name is not relevant, use a meaningful name
    - Use a meaningful app description
      - Save the client id, also the secret
      - Set the Redirect URI "http://localhost:1337/" under "Edit Settings"

# Variables
* reward_name is the reward name on twitch 
* streamer_name is your name on twitch
* spotify_playlist is the playlist id from spotify 
