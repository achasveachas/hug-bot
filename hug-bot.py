import os
from random import choice
from atproto import Client
import giphy

from statuses import STATUSES

video_filename, alt_text = giphy.download_random_gif()

client = Client()
client.login(os.environ['BLUESKY_USERNAME'], os.environ['BLUESKY_PASSWORD'])

with open(video_filename, 'rb') as f:
    video_data = f.read()
    client.send_video(text=choice(STATUSES), video=video_data, video_alt=alt_text)

os.remove(video_filename)
