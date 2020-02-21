import time
import urllib.request
import os
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
hug_filename = "hug.gif"

def download_random_gif():
    giphy_api = giphy_client.DefaultApi()
    giphy_api_key = environ['giphy_api_key']
    tag = 'hug'
    fmt = 'json'
    api_response = giphy_api.gifs_random_get(giphy_api_key, tag=tag, fmt=fmt)
    
    urllib.request.urlretrieve(api_response.data.image_url, hug_filename)

download_random_gif()
# Twitter has a max upload size of 15MB
while os.path.getsize(hug_filename) > 15728640:
    download_random_gif()

gif_upload = api.media_upload(hug_filename)
api.update_status("This account is under construction, please excuse our appearance", media_ids=[gif_upload.media_id])

os.remove(hug_filename)