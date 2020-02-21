import time
import urllib.request
import giphy_client
from os import environ

def download_random_gif():
    giphy_api = giphy_client.DefaultApi()
    giphy_api_key = environ['giphy_api_key']
    tag = 'hug'
    fmt = 'json'
    api_response = giphy_api.gifs_random_get(giphy_api_key, tag=tag, fmt=fmt)
    
    urllib.request.urlretrieve(api_response.data.image_url,'hug.gif')

download_random_gif()