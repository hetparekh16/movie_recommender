import pandas as pd
from dotenv import load_dotenv
import os
import requests
from recommender.config import BASE_URL, GENRE_URL, SERIES_URL

load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_crew(movie_id):
    """
    Fetch crew details for a given movie ID.
    """
    credits_url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {"api_key": API_KEY}
    response = requests.get(credits_url, params=params)
    if response.status_code == 200:
        crew_data = response.json().get("crew", [])
        crew_details = {}
        for crew_member in crew_data:
            job = crew_member.get("job", "Unknown")
            if job in ["Director"]:  # Focus on key roles
                crew_details[job] = crew_details.get(job, []) + [
                    crew_member.get("name", "Unknown")
                ]
        return {key: ", ".join(value) for key, value in crew_details.items()}
    else:
        print(f"Failed to fetch crew for movie_id {movie_id}: {response.status_code}")
        return {}
