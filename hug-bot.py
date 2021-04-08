import os
from random import choice
from tweepy_client import twitter_api
import giphy

from statuses import STATUSES

giphy.download_random_gif()
gif_filename = "hug.gif"

api = twitter_api()
gif_upload = api.media_upload(gif_filename, chunked=True)
api.create_media_metadata(media_id=gif_upload.media_id, alt_text="randomly generated gif, hopefully depicting a hug. ")
status = api.update_status(
    status=choice(STATUSES),
    media_ids=[gif_upload.media_id],
)
print("Sent Tweet ID: " + status.id_str)
os.remove(gif_filename)
