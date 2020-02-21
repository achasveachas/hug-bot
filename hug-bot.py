import time
import urllib.request
from os import environ
import giphy_client
import tweepy

twitter_api_key = environ['twitter_api_key']
twitter_api_secret = environ['twitter_api_secret']
twitter_access_token = environ['twitter_access_token']
twitter_access_secret = environ['twitter_access_secret']
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)
api = tweepy.API(auth)

api.update_status("Hello World")

def download_random_gif():
    giphy_api = giphy_client.DefaultApi()
    giphy_api_key = environ['giphy_api_key']
    tag = 'hug'
    fmt = 'json'
    api_response = giphy_api.gifs_random_get(giphy_api_key, tag=tag, fmt=fmt)
    
    urllib.request.urlretrieve(api_response.data.image_url,'hug.gif')