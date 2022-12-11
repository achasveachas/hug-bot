from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import urlencode
import os
from os import environ
import json
import giphy_client

def download_random_gif():
    gif_filename = "hug.gif"

    giphy_random_url = 'https://api.giphy.com/v1/gifs/random'
    giphy_api_key = environ['GIPHY_API_KEY']
    tags = ['hug', 'hugging']
    giphy_params = {
        'api_key': giphy_api_key,
        'tag': ' '.join(tags),
        'rating': 'g',
        'fmt': 'json',
    }
    encoded_params = urlencode(giphy_params)

    api_response = urlopen(giphy_random_url + "?" + encoded_params)
    gif_data = json.loads(api_response.read())
    gif_url = gif_data['data']['images']['downsized_large']['url']

    open(gif_filename, 'w')
    urlretrieve(gif_url, gif_filename)
    
    print("Downloaded GIF ID: {}, GIF URL: {}".format(gif_data['data']['id'], gif_url))