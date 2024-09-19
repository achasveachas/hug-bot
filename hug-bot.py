import os
from random import choice
from atproto import Client
import giphy

from statuses import STATUSES

giphy.download_random_gif()
gif_filename = "hug.mp4"

client = Client()
client.login(os.environ['BLUESKY_USERNAME'], os.environ['BLUESKY_PASSWORD'])

with open(gif_filename, 'rb') as f:
    img_data = f.read()
    client.send_video(text=choice(STATUSES), video=img_data, video_alt='Img alt')

os.remove(gif_filename)
