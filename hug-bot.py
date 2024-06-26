import os
from random import choice
from atproto import Client
import giphy

from statuses import STATUSES

giphy.download_random_gif()
gif_filename = "hug.gif"

client = Client()
client.login(os.environ['BLUESKY_USERNAME'], os.environ['BLUESKY_PASSWORD'])

with open(gif_filename, 'rb') as f:
    img_data = f.read()
    client.send_image(text='test', image=img_data, image_alt='Img alt')

#os.remove(gif_filename)
