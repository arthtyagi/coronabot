import requests
import tweepy
import time
import datetime

# Keys for the authentication process
ConsumerKey = 'Key'
ConsumerSecret = 'Key'
AccessToken = 'Key'
AccessTokenSecret = 'Key'
 
# Authentication process using the keys
auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
 
# Creation of the actual interface using authentication
api = tweepy.API(auth)

# Infinite loop, tweets once every 24 hours
while True:
    try:
        # Retrievel of API
        response = requests.get("https://coronavirus-tracker-api.herokuapp.com/all")

        # Fetches JSON
        data = response.json()
        # Fetches the 'latest' node from the API
        LatestData = data['latest']

        # Current Time
        CurrentTime = datetime.datetime.now().time()
        
        # Sub nodes from the 'latest' node are fetched along with the current date/time and used in the tweet
        tweet = "The Latest Coronavirus statistics are as follows: \n Tweeted: " + CurrentTime +  "\n Confirmed: " + str(LatestData['confirmed']) +"" + "\n Deaths: " + str(LatestData['deaths']) + "\n Recovered: " + str(LatestData['recovered']) +  "\n #COVID19 #COVID-19 #Covid_19 #Coronavirus #CoronavirusPandemic"        
        print(tweet)        
        api.update_status(tweet)
        time.sleep(4320)
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)
        
    except StopIteration:
        break
