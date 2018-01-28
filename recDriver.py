
from userData    import *
from filmData    import * 
from musicData   import * 
from bookData    import *
from utilFuns    import *
from numpy       import * 
from collections import OrderedDict

from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

import operator


user_data = outputUserData()
film_data = outputFilmData()
music_data = outputMusicData()
book_data = outputBookData()

def showFilmMatch():
    return list(film_data[0].items())[:3]

print(showFilmMatch())
#This function is used to receive and analyze
#the last 200 tweets of a Twitter handle using
#the Watson PI API
user_analysis = dict(sort_by_value(flatten(PersonalityInsights(username="277d208a-0a15-479f-92cb-feca3385165a", 
                                  password="UDxJDKdFGQjd").profile(user_data))))



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

#def match_user_media(user_analysis, rankings):



# #Analyze the user's tweets using the Watson PI API
# #user1_result = analyze(user1_handle)
# #user2_result = analyze(user2_handle)

# #Flatten the results received from the Watson PI API

# #Compare the results of the Watson PI API by calculating
# #the distance between traits
# #compared_results = compare(user1,user2)

# #Sort the results
# #sorted_results = sorted(compared_results.items(), key=operator.itemgetter(1))

# #Print the results to the user
# #for keys, value in sorted_results[:5]:
#     print(keys) ,
#     print(user1[keys]),
#     print('->'),
#     print(user2[keys]),
#     print('->'),
#     print(compared_results[keys])