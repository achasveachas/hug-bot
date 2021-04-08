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
    while os.path.getsize(gif_filename) == 0 or os.path.getsize(gif_filename) > 14648 * 1024:
        api_response = giphy_api.gifs_random_get(giphy_api_key, rating=rating, tag=tag, fmt=fmt)
        urllib.request.urlretrieve(api_response.data.image_url, gif_filename)
    print("Downloaded GIF ID: {}, GIF URL: {}".format(api_response.data.id, api_response.data.image_url))