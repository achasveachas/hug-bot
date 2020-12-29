import time
import urllib.request
import os
import sys
from os import environ
from datetime import datetime
from random import choice
import giphy_client
import tweepy

from statuses import STATUSES

gif_filename = "hug.gif"

def twitter_api():
    twitter_api_key = environ['twitter_api_key']
    twitter_api_secret = environ['twitter_api_secret']
    twitter_access_token = environ['twitter_access_token']
    twitter_access_secret = environ['twitter_access_secret']
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    return tweepy.API(auth)

def download_random_gif():
    giphy_api = giphy_client.DefaultApi()
    giphy_api_key = environ['giphy_api_key']
    tags = ['hug', 'hugging']
    tags.extend(sys.argv[1:])
    tag = ' '.join(tags)
    rating = 'g'
    fmt = 'json'
    open(gif_filename, 'w')
    # Twitter has a max upload size of 15MB
    # TODO: tweepy has a bug and doesn't let more than ~5mb, update the max when they fix it
    # https://github.com/tweepy/tweepy/pull/1414 (hopefully?)
    while os.path.getsize(gif_filename) == 0 or os.path.getsize(gif_filename) > 5242880:
        api_response = giphy_api.gifs_random_get(giphy_api_key, rating=rating, tag=tag, fmt=fmt)
        urllib.request.urlretrieve(api_response.data.image_url, gif_filename)
    print("Downloaded GIF ID: {}, GIF URL: {}".format(api_response.data.id, api_response.data.image_url))

def tweet_gif():
    api = twitter_api()
    gif_upload = api.media_upload(gif_filename)
    api.create_media_metadata(media_id=gif_upload.media_id, alt_text="randomly generated gif, hopefully depicting a hug. ")
    status = api.update_status(
        status=choice(STATUSES),
        media_ids=[gif_upload.media_id],
    )
    print("Sent Tweet ID: " + status.id_str)
    os.remove(gif_filename)

def main():
    download_random_gif()
    tweet_gif()

if __name__ == "__main__":
    main()