import time
import urllib.request
import os
from os import environ
from datetime import datetime
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
    rating = 'g'
    open(hug_filename, 'w')
    # Twitter has a max upload size of 15MB
    while os.path.getsize(hug_filename) == 0 or os.path.getsize(hug_filename) > 15000000:
        api_response = giphy_api.gifs_random_get(giphy_api_key, tag=tag, fmt=fmt, rating=rating)
        urllib.request.urlretrieve(api_response.data.image_url, hug_filename)

def tweet_gif():
    gif_upload = api.media_upload(hug_filename)
    api.update_status(
        status="Here! Have a hug!\n\n[gif-alt: randomly generated gif hopefully depicting a hug]",
        media_ids=[gif_upload.media_id],
    )
    os.remove(hug_filename)

def main():
    while True:
        download_random_gif()
        tweet_gif()
        time.sleep(10800)

if __name__ == "__main__":
    main()