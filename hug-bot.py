from giphy import download_random_gif
from time import sleep
from tweet import tweet_gif

def main():
    while True:
        download_random_gif(gif_filename)
        tweet_gif(gif_filename)
        time.sleep(10800)


if __name__ == "__main__":
    main()
