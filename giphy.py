import urllib.request
import os
from os import environ
import giphy_client

def download_random_gif():
    gif_filename = "hug.gif"

    giphy_api = giphy_client.DefaultApi()
    giphy_api_key = environ['giphy_api_key']
    tags = ['hug', 'hugging']
    tag = ' '.join(tags)
    rating = 'g'
    fmt = 'json'
    open(gif_filename, 'w')
    # Twitter has a max upload size of 15MB
    # TODO: tweepy has a bug and doesn't let more than ~5mb, update the max when they fix it
    # https://github.com/tweepy/tweepy/pull/1486 (hopefully?)
    while os.path.getsize(gif_filename) == 0 or os.path.getsize(gif_filename) > 5242880:
        api_response = giphy_api.gifs_random_get(giphy_api_key, rating=rating, tag=tag, fmt=fmt)
        urllib.request.urlretrieve(api_response.data.image_url, gif_filename)
    print("Downloaded GIF ID: {}, GIF URL: {}".format(api_response.data.id, api_response.data.image_url))