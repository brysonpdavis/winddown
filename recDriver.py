# ..................................................................
# : Wind Down: Music, Movie, & Book Recs for your Psyche           :
# : B. Davis, A. M. Rahman, K. Noelsaint, G. Ren | hack@Brown '18  :
# : winddown/recDriver.py                                          :
# : -- Contains API calls to Watson for user personality insights  :
# :    and match users with potential media                        :
# :................................................................:

#from userData    import *
#from songData    import *
from filmData    import * 
from bookData    import *
from utilFuns    import *
from numpy       import * 
from collections import OrderedDict
from random      import choice

from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

import operator, pickle

# API Calls for analysis

def analyzeUser(user_text):
    return dict(sort_by_value(flatten(PersonalityInsights(username="277d208a-0a15-479f-92cb-feca3385165a", 
                                  password="UDxJDKdFGQjd").profile(user_text))))



# with open('songdata.pkl', 'rb') as f:
#     music_data = pickle.load(f)


def analyzeMedia(media_list):
    for media in media_list: 
        media["analysis"]=sort_by_value(flatten(PersonalityInsights(username="277d208a-0a15-479f-92cb-feca3385165a", 
                                    password="UDxJDKdFGQjd").profile(media["excerpt"])))
    return media_list


#book_data_analyses = analyzeMedia(book_data)
#music_data_analyses = analyzeMedia(music_data)


#print(film_data_analyses)

# Compare the results from the Watson PI API
# def compare(user_analysis, media_analyses):
#     compared_data = {}
#     for keys in dict1:
#             if dict1[keys] != dict2[keys]:
#                 compared_data[keys] = abs(dict1[keys] - dict2[keys])
#     return compared_data


def rank_media(media_analyses):
    rankings = []
    for med_a in media_analyses:
        print(med_a["analysis"])

        media_analyses['hexranks'] = best6(dict(med_a["analysis"]))

    return media_analyses

#----------------------------------------------------------------------------#
# THE OUTPUT CORNER
#

'''this returns recomendation given user_pref which 
is top 3 choices and movies which is list of top 6 movies allwords_frequency
attributes '''
def recom(user_pref,movies): 
    move=[]
    new_list=[]
    for i in user_pref:
        for j in movies:
            if i not in j:
                move.append(j)
    for x in movies:
        if x not in move:
            new_list.append(x)
    if new_list==[]:
        return "random"
    elif len(new_list)>1:
        return random.choice(new_list)
    else:
        return new_list[0] 


def showFilmMatch():
    '''
    Returns a list of tuples in order of:
    title, date, genre, synopsis
    '''
    return list(((choice(getFilmData())).items()))

# def showSongMatch(user_input):
#     '''
#     Returns a list of tuples in order of:
#     title, artist, genre
#     '''
#     return recom(best3(analyzeUser(user_input)), rank_media(film_data_analyses))

#print(showSongMatch())

def driver(user_input):
    '''
    Given user_input,
    returns results!
    '''
    out_dict = {}
    out_dict['Film'] = showFilmMatch()
#    out_dict['Song'] = showSongMatch(user_input)