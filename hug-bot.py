import time
import urllib.request
import os
from os import environ
from datetime import datetime
from random import choice
import giphy_client
import tweepy

from statuses import STATUSES

twitter_api_key = environ['twitter_api_key']
twitter_api_secret = environ['twitter_api_secret']
twitter_access_token = environ['twitter_access_token']
twitter_access_secret = environ['twitter_access_secret']
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)
api = tweepy.API(auth)
gif_filename = "hug.gif"

def download_random_gif():
    giphy_api = giphy_client.DefaultApi()
    giphy_api_key = environ['giphy_api_key']
    tag = 'hug'
    fmt = 'json'
    rating = 'g'
    open(gif_filename, 'w')
    # Twitter has a max upload size of 15MB
    while os.path.getsize(gif_filename) == 0 or os.path.getsize(gif_filename) > 15000000:
        api_response = giphy_api.gifs_random_get(giphy_api_key, tag=tag, fmt=fmt, rating=rating)
        urllib.request.urlretrieve(api_response.data.image_url, gif_filename)

def tweet_gif():
    gif_upload = api.media_upload(gif_filename)
    api.create_media_metadata(media_id=gif_upload.media_id, alt_text="randomly generated gif, hopefully depicting a hug")
    api.update_status(
        status=choice(STATUSES),
        media_ids=[gif_upload.media_id],
    )
    os.remove(gif_filename)

def main():
    while True:
        download_random_gif()
        tweet_gif()
        time.sleep(10800)

if __name__ == "__main__":
    main()