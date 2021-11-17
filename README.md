# playlist-data
automated spotify playlist data display using requests and spotipy library. short introductory project undertaken to get a better understanding of the spotify API 

## requirements
download the requests library using the command line:
```
python -m pip install requests
```
... and download the spotipy library using the command line:
```
pip install spotipy --upgrade
```

## files
### playlist.py
**playlist.py** is the main file that contains functions for gaining the application's access token and processing the data for the playlist.
### secrets.py
**secrets.py** stores the client ID and client secret of the application the user will have to create in the developer dashboard on spotify's developer page.

## usage
upon running the *playlist.py* file, the user will be prompted to input a spotify playlist URL (given the format "https://open.spotify.com/playlist/playlist-id-here"). the program will then intake all data from the given playlist and export the data to file *tracklist.json* and will extract artist and track names for each song in the playlist for output into the console. 

