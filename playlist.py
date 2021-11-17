import requests
import base64
import json
from secrets import clientID
from secrets import clientSecret

# endpoint #
authURL = "https://accounts.spotify.com/api/token" 

# authorization header for credential specification #
authHeader = {}

# hold grant type for access token #
authData = {}

# base64 encoder for app client ID and secret #
def accessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}" 
    messageBytes = message.encode('ascii')
    base64bytes = base64.b64encode(messageBytes)
    base64message = base64bytes.decode('ascii')

    # create authorization tag for header with encoded message #
    authHeader['Authorization'] = "Basic " + base64message

    # create grant type tag #
    authData['grant_type'] = "client_credentials"

    # !!! be sure to have requests library installed correctly !!! #
    # !!! have cacert.pem copied to your certifications folder !!! #
    res = requests.post(authURL, headers=authHeader, data=authData)

    # print(base64message) 

    # print(res)

    # create access token #
    resObj = res.json()

    token = resObj['access_token']
    
    return token


def playlistInfo(token, playlistID):
    # referenced from API endpoint reference #
    playlist = f"https://api.spotify.com/v1/playlists/{playlistID}"
    
    # get authorization header #
    getHeader = {"Authorization": "Bearer " + token}
    
    res = requests.get(playlist, headers=getHeader)
    
    playlistObj = res.json()
    
    return playlistObj

# API request #
token = accessToken(clientID, clientSecret)

playlistURL = input("Enter playlist URL: ")

playlistID = playlistURL.replace("https://open.spotify.com/playlist/", "")

tracklist = playlistInfo(token, playlistID)

# write data into json file for extraction later #
with open('tracklist.json', 'w') as f:
    json.dump(tracklist, f)

# extract data from json file #
for track in tracklist['tracks']['items']:
    for a in track['track']['artists']:
        artist = a['name']
    title = track['track']['name']
    print(f"{artist} - {title}")
    
