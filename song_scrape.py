import billboard
from pylyrics3 import pylyrics3

bill = billboard.ChartData
pyly = pylyrics3

genres = ['rb_hip_hop', 'rap', 'rock', 'latin', 'country']


country_songs = bill('greatest-country-songs', date = None, fetch = True).entries

latin_songs = bill('greatest-hot-latin-songs', date = None, fetch = True).entries

rb_hip_hop_songs = bill('greatest-r-b-hip-hop-songs', date = None, fetch = True).entries

rap_songs = bill('rap-song', date = None, fetch = True).entries

rock_songs = bill('greatest-of-all-time-pop-songs', date = None, fetch = True).entries
"""
def clean_art (artist):
    if ("Duet" in artist):
        rest = artist.split("Duet", 1)[0]
        return rest
    elif "With" in artist:
        rest = artist.split("With", 1)[0]
        print(rest)
        return rest
    elif ("Feat" in artist):
        rest = artist.split("Feat", 1)[0]
        return rest
    elif ("Featuring" in artist):
        rest = artist.split("Featuring", 1)[0]
        return rest

    else:
        return artist
"""


def char_look(char, string):
    for i in range(0, len(string)):
        if char == string[i]:
            return True
    return False

def check(artist, title):
    return not(("With" in artist) or ("Feat" in artist) or ("Featuring" in artist) or ("&" in artist) or (char_look("/",artist)) or (char_look("/",title)))

def get_lyrics (artist, title):
    return pyly.get_song_lyrics(artist, title)

def create_songs():
    songs = []
    for song in country_songs:
        artist = song.artist
        title = song.title
        if check(artist,title):
            cont = get_lyrics(artist, title)
            songs.append({'title': title, 'misc': artist, 'excerpt': cont, 'genre': "Country"})
        else:
            pass
    for song in rb_hip_hop_songs:
        artist = song.artist
        title = song.title
        if check(artist,title):
            cont = get_lyrics(artist, title)
            songs.append({'title': title, 'misc': artist, 'excerpt': cont, 'genre': "R&B/Hip Hop"})
        else:
            pass
    for song in rap_songs:
        artist = song.artist
        title = song.title
        if check(artist,title):
            cont = get_lyrics(artist, title)
            songs.append({'title': title, 'misc': artist, 'excerpt': cont, 'genre': "Rap"})
        else:
            pass
    for song in rock_songs:
        artist = song.artist
        title = song.title
        if check(artist,title):
            cont = get_lyrics(artist, title)
            songs.append({'title': title, 'misc': artist, 'excerpt': cont, 'genre': "Rock/Pop"})
        else:
            pass
    for song in latin_songs:
        artist = song.artist
        title = song.title
        if check(artist,title):
            cont = get_lyrics(artist, title)
            songs.append({'title': title, 'misc': artist, 'excerpt': cont, 'genre': "Latin"})
        else:
            pass
    return songs

song_list = create_songs()
print(len(song_list))
