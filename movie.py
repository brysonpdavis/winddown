import twitter

def get_user_tweets(handle):
	#The Twitter API credentials
    twitter_consumer_key = 'w2YWOpLzlH5STiMgDZFuCnqzk'
    twitter_consumer_secret = 'nhJmbFHCwr7PzRAMaMnhu8BZuLDUW2GqAytDCNGOR6SK7l57v5'
    twitter_access_token = '927185807630393345-Ofr60iCq3UxcqW5ezFQjirXIMYlAz3O'
    twitter_access_secret = 'cFE0bEhvf3LAgHLQduCHa0I2DAuP6zhxlc68cIU1dLbUN'

    #Invoking the Twitter API
    twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token,
                  access_token_secret=twitter_access_secret)

    #Retrieving the last 200 tweets from a user
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

    text = ""
    for s in statuses:
        if (s.lang =='en'):
            text += str(s.text.encode('utf-8'))

    return text

# ..................................................................
# : Wind Down: Music, Movie, & Book Recs for your Psyche           :
# : B. Davis, A. M. Rahman, K. Noelsaint, G. Ren | hack@Brown '18  :
# : winddown/filmData.py                                           :
# : -- Contains API calls to Watson for user personality insights  :
# :    and match users with potential media                        :
# :................................................................:

import json, http.client, operator
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
#from userData import *


# MovieDB Genre Values
genre_dict = {"action": 28, "adventure": 12, "documentary": 99, "drama": 18, "historical": 36, "horror": 27, "music": 10402, "romance": 10749, "science": 878, "war": 10752}


def getGenres(given_text):
    genres = []
    personality_insights = PersonalityInsightsV3(
        version='2016-10-20',
        username='ab71aaa2-ccaa-4b0e-abcf-594e37a04da6',
        password='J0Ncu5mKPBTn')

    #source = open(given_text, "r")
    #movie_script = source.read().replace("\n", "")

    profile = personality_insights.profile(
            given_text, content_type='text/plain',
            raw_scores=True, consumption_preferences=True)
    preferences = profile["consumption_preferences"][4]["consumption_preferences"]

    for preference in preferences:
        score = preference["score"]
        if (score > 0):
            genre = preference["consumption_preference_id"].split("_")[3]
            genres.append(genre)
    return (genres)


def createMovie(raw_data, genre):
    movie = {}
    movie["title"] = raw_data["original_title"]
    movie["misc"] = raw_data["release_date"]
    movie["genre"] = genre
    movie["excerpt"] = raw_data["overview"]
    return movie


def getMovies(genres):
    genre_count = {}
    movies = []

    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    conn.request("GET", "/3/genre/" + str(genre_dict[genres[0]]) + "/movies?sort_by=created_at.asc&include_adult=false&language=en-US&api_key=3486199bc5adae4346ec39a5fd842cd3", payload)
    res = conn.getresponse()
    data = json.loads(res.read())["results"]

    for i in range(len(data)):
        movie = data[i]
        genre_count[i] = len(movie["genre_ids"])

    sorted_genre_count = sorted(genre_count.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(10):
        curr_movie = createMovie(data[sorted_genre_count[i][0]], genres[0])
        movies.append(curr_movie)

    return movies

def outputFilmData(user_text):
    genres = getGenres(user_text)
    return getMovies(genres)

def get_movie_list(tweets):
    return outputFilmData(tweets)
