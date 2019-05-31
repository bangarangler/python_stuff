playlist = {
  "title": "J's Mix",
  "author": "Jon",
  "songs": [
    {"title": 'song1', 'artist': ['one'], 'duration': 2.4},
    {"title": 'song2', 'artist': ['bb', "kitty"], 'duration': 5.3},
    {"title": 'song3', 'artist': ["kitty"], 'duration': 2.0}
  ]
}

total_length = 0
for song in playlist['songs']:
  total_length += song['duration']
  print(total_length)


