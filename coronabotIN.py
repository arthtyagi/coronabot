import requests
import tweepy
import time
import datetime

# Keys for the authentication process 
ConsumerKey = 'key'     #  input keys within these marks
ConsumerSecret = 'key'
AccessToken = 'key'
AccessTokenSecret = 'key'
 
# Authentication process using the keys
auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
 
# Creation of the actual interface using authentication
api = tweepy.API(auth)

# Infinite loop, tweets once every 24 hours
while True:
    try:
        # Retrievel of API
        response = requests.get('https://covid19.mathdro.id/api/countries/IN')
        responseJson = response.json();
        confirmed = responseJson['confirmed']['value']
        recovered = responseJson['recovered']['value']
        deaths = responseJson['deaths']['value'] 
        # Current Time
        CurrentTime = datetime.datetime.now().time()
        
        # Sub nodes from the 'latest' node are fetched along with the current date/time and used in the tweet
        tweet1 = "The Latest Coronavirus statistics from the India ⚠️ are as follows: \n Confirmed: " + str(confirmed) + "" + "\n Deaths: " + str(deaths) + "" + "\n Reliable data from https://covid19.mathdro.id/api/countries/IN" "\n #COVID19 #COVID-19 #Covid_19 #Coronavirus #CoronavirusPandemic #India #staysafe"
        print(tweet1)        
        api.update_status(tweet1)
        
        time.sleep(3600)
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)
        
    except StopIteration:
        break
