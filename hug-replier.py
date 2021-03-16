import giphy
import os
from tweepy_client import twitter_api

gif_filename = "hug.gif"

api = twitter_api()
tweets = api.search(q="need a hug", result_type="recent", count=100)
tweet_ids = [tweet.id for tweet in tweets]

for i, tweet in enumerate(tweets, start=1):
    if hasattr(tweet, "retweeted_status") and tweet.retweeted_status.id in tweet_ids:
        print(f"skipping retweet {tweet.id}")
        continue
    try:
        giphy.download_random_gif()
        gif_upload = api.media_upload(gif_filename)
        api.create_media_metadata(media_id=gif_upload.media_id, alt_text="randomly generated gif, hopefully depicting a hug. ")
        api.update_status(
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True,
            media_ids=[gif_upload.media_id],
        )
        print(f"Replied to tweet number {i}, id: {tweet.id}")
    except Exception as e:
        print(f"An error occured while replying to tweet id: {tweet.id}\n{e.message}")
    finally:
        os.remove(gif_filename)
