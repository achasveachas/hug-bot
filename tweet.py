from auth import authenticate_api
from os import remove
from random import choice
from statuses import STATUSES


def tweet_gif(gif_name: str):
    try:
        api = authenticate_api()
        gif_upload = api.media_upload(gif_name)
        api.create_media_metadata(
            media_id=gif_upload.media_id,
            alt_text="randomly generated gif, hopefully depicting a hug"
        )
        status = api.update_status(
            status=choice(STATUSES),
            media_ids=[gif_upload.media_id]
        )

        print("Sent Tweet ID: " + status.id_str)

        remove(gif_name)
    except Exception:
        print(f"An error occurred when attempting to download a tweet the gif.")
