class Song:
    def __init__(self, type_list, name, data):
        self.type_list = type_list
        self.name = name
        self.data = data

n = int(input())
songs = []

for _ in range(n):
    data = input().split('_')
    song = Song(data[0], data[1], data[2])
    songs.append(song)

type_list_filter = input()

if type_list_filter == 'all':
    for song in songs:
        print(song.name)
else:
    for song in songs:
        if song.type_list == type_list_filter:
            print(song.name)
