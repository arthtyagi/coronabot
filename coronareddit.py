import praw
import tweepy
import time


#enter your information from the reddit dev dashboard
client_id = -
client_secret = -
user_agent = -
username = -
password = -

reddit = praw.Reddit(
    client_id = client_id,
    client_secret = client_secret,
    user_agent = user_agent,
    username = -
    password = -
    )

# choose your subreddit
subred = reddit.subreddit("coronavirus")

#enter your consumer tokens here from the twitter dev dashboard
consumer_key = -
consumer_secret = -
access_token = -
access_token_secret = -

#oath info
auth = tweepy.OAuthHandler(
    consumer_key,
    consumer_secret,
)

auth.set_access_token(
    access_token,
    access_token_secret,
)
api = tweepy.API(auth)
user = api.me()

def new_tweet():
    """function that takes a stream from a subreddit api praw
    and posts it with the tweepy api"""
    while True:
        try:
            for submission in reddit.subreddit('coronavirus').stream.submissions():
                #updates twitter status with the title of the post and url in the post
                #credit the poster with submission.author
                api.update_status(
                    str(submission.title) + '\n' + 
                    str(submission.url) + '\n'+
                    'reddit user:'+
                    str(submission.author)
                )
                #tweet message to make sure that it is running 
                print('tweeted')
                time.sleep(300) #select the time between posts in seconds
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            pass
        
new_tweet()
