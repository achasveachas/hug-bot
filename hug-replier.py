import giphy
import os
from tweepy_client import twitter_api

gif_filename = "hug.gif"

api = twitter_api()
tweets = api.search(q="I need a hug", result_type="recent", count=100)
tweet_ids = set()
for tweet in tweets:
    if hasattr(tweet, "retweeted_status"):
        tweet_ids.add(tweet.retweeted_status.id)
    else:
        tweet_ids.add(tweet.id)

for i, id in enumerate(tweet_ids, start=1):
    try:
        giphy.download_random_gif()
        gif_upload = api.media_upload(gif_filename, chunked=True)
        api.create_media_metadata(media_id=gif_upload.media_id, alt_text="randomly generated gif, hopefully depicting a hug. ")
        api.update_status(
            status="",
            in_reply_to_status_id=id,
            auto_populate_reply_metadata=True,
            media_ids=[gif_upload.media_id],
        )
        print(f"Replied to tweet number {i}, id: {id}")
    except Exception as e:
        print(f"An error occured while replying to tweet id: {id}\n{e}")
    finally:
        os.remove(gif_filename)
