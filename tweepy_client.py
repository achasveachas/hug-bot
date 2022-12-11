from os import environ
import tweepy

from statuses import STATUSES

def twitter_api():
    twitter_api_key = environ['TWITTER_API_KEY']
    twitter_api_secret = environ['TWITTER_API_SECRET']
    twitter_access_token = environ['TWITTER_ACCESS_TOKEN']
    twitter_access_secret = environ['TWITTER_ACCESS_SECRET']
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    return tweepy.API(auth)
