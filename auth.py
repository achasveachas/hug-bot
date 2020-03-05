import tweepy
from os import environ

twitter_api_key = environ['twitter_api_key']
twitter_api_secret = environ['twitter_api_secret']
twitter_access_token = environ['twitter_access_token']
twitter_access_secret = environ['twitter_access_secret']


def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
        auth.set_access_token(twitter_access_token, twitter_access_secret)
        return tweepy.API(auth)
    except Exception:
        print(f"An error occurred when attempting to authenticate with the twitter API.")
