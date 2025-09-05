import os
from random import choice
from atproto import Client
import giphy

from statuses import STATUSES

gif_filename, alt_text = giphy.download_random_gif()

client = Client()
client.login(os.environ['BLUESKY_USERNAME'], os.environ['BLUESKY_PASSWORD'])

with open(gif_filename, 'rb') as f:
    img_data = f.read()
    client.send_video(text=choice(STATUSES), video=img_data, video_alt=alt_text)

os.remove(gif_filename)
