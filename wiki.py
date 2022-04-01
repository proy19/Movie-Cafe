import requests
import os

# Function to get the wiki link from the API
def get_wiki_link(movie_title):
    movie = movie_title

    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/title/{movie}")

    response_json = response.json()

    wiki_id = response_json["items"][0]["page_id"]
    wiki_url = f"https://en.wikipedia.org/?curid={wiki_id}"

    return wiki_url
