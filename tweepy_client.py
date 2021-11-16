from os import environ
import tweepy

from statuses import STATUSES

def twitter_api():
    twitter_api_key = environ['twitter_api_key']
    twitter_api_secret = environ['twitter_api_secret']
    twitter_access_token = environ['twitter_access_token']
    twitter_access_secret = environ['twitter_access_secret']
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    return tweepy.API(auth)
