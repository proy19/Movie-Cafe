import requests
import os
import random
from wiki import get_wiki_link
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Function to get all the movie data from the API
def get_movie_data():

    movie_id_list = {
        "9655": "She%27s_the_Man",
        "8835": "Legally_Blonde",
        "671": "Harry_Potter_and_the_Philosopher%27s_Stone_(film)",
        "597": "Titanic_(1997_film)",
        "10625": "Mean_Girls",
        "38757": "Tangled",
        "1726": "Iron_Man",
        "396535": "Train_to_Busan",
    }
    id = random.choice(list(movie_id_list))
    BASE_URL = f"https://api.themoviedb.org/3/movie/{id}"
    params = {
        "api_key": os.getenv("API_KEY"),
    }

    response = requests.get(
        BASE_URL,
        params=params,
    )

    response_json = response.json()
    title = response_json["original_title"]
    genre = response_json["genres"][0]["name"]
    tagline = response_json["tagline"]
    image_base_url = "https://image.tmdb.org/t/p/original/"
    image_path = response_json["poster_path"]
    poster = image_base_url + image_path
    wiki_url = get_wiki_link(movie_id_list[id])

    return title, genre, tagline, poster, wiki_url, id
