from flask import Flask, request, render_template
#from userData import *
from recDriver import *
import twitter

app = Flask(__name__)

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


@app.route('/', methods = ['POST', 'GET'])
def home():
	return render_template('index.html')

@app.route('/result', methods = ['POST'])
def process_handle():
	if request.method == 'POST':
		user_handle = request.form.get('handle')
		print(user_handle)
		result = get_user_tweets(user_handle)
		print(result)
		return '''<h1> Your tweets!: {}</h1>'''.format(result)

if __name__ == '__main__':
    app.run(debug=True)
