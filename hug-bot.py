from giphy import download_random_gif
from time import sleep
from tweet import tweet_gif

gif_filename = "hug.gif"
statuses = []

def twitter_api():
    twitter_api_key = environ['twitter_api_key']
    twitter_api_secret = environ['twitter_api_secret']
    twitter_access_token = environ['twitter_access_token']
    twitter_access_secret = environ['twitter_access_secret']
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    return tweepy.API(auth)


def main():
    while True:
        download_random_gif(gif_filename)
        tweet_gif(gif_filename)
        time.sleep(10800)


if __name__ == "__main__":
    main()
