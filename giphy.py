from giphy_client import DefaultApi
from os import environ, path
from urllib.request import urlretrieve


def download_random_gif(gif_name: str):
    try:
        giphy_api = DefaultApi()
        open(gif_name, 'w')

        while path.getsize(gif_name) <= 15000000:
            api_response = giphy_api.gifs_random_get(
                environ['giphy_api_key'],
                tag="hug",
                fmt="json",
                rating="g"
            )
            urlretrieve(
                api_response.data.image_url,
                gif_name
            )

        print(
            f"Downloaded GIF ID: {api_response.data.id}, GIF URL: {api_response.data.image_url}"
        )
    except Exception:
        print(f"An error occurred when attempting to download a gif using the giphy API.")
