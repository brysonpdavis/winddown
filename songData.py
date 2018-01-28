# ..................................................................
# : Wind Down: Music, Movie, & Book Recs for your Psyche           :
# : B. Davis, A. M. Rahman, K. Noelsaint, G. Ren | hack@Brown '18  :
# : winddown/songData.py                                           :
# : -- Contains API calls to Watson for user personality insights  :
# :    and match users with potential media                        :
# :................................................................:

import billboard
#from billboard import ChartData
import pylyrics3
import pickle

bill = billboard.ChartData
pyly = pylyrics3

country_songs = bill('greatest-country-songs', date = None, fetch = True).entries
latin_songs = bill('greatest-hot-latin-songs', date = None, fetch = True).entries
rb_hip_hop_songs = bill('greatest-r-b-hip-hop-songs', date = None, fetch = True).entries
rap_songs = bill('rap-song', date = None, fetch = True).entries
rock_songs = bill('greatest-of-all-time-pop-songs', date = None, fetch = True).entries


def char_look(char, string):
    for i in range(0, len(string)):
        if char == string[i]:
            return True
    return False


def check(artist, title):
    return not(("With" in artist) or ("Feat" in artist) or ("Featuring" in artist) or ("&" in artist) or (char_look("/",artist)) or (char_look("/",title)))


def get_lyrics (artist, title):
    if (pyly.get_song_lyrics(artist, title) == None):
        return 'a ' * 100
    else:
        return (pyly.get_song_lyrics(artist, title) * 2)


def outputSongData():
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
    return songs[100]

def package_songs():
    with open('songdata.pkl', 'wb') as f:
        pickle.dump(outputSongData(), f)