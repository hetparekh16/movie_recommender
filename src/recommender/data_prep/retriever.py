import pandas as pd
from dotenv import load_dotenv
import os
import requests
from recommender.config import BASE_URL, GENRE_URL, SERIES_URL, MOVIE_URL

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


def fetch_movies_by_language(
    total_pages, genre_mapping, language, include_adult=False, include_video=False
):
    movies = []
    for page in range(1, total_pages + 1):
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "sort_by": "popularity.desc",
            "page": page,
            "include_adult": include_adult,
            "include_video": include_video,
            "with_original_language": language,
        }
        response = requests.get(MOVIE_URL, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            for item in results:
                genres = [
                    genre_mapping.get(genre_id, "Unknown")
                    for genre_id in item.get("genre_ids", [])
                ]
                movie_id = item.get("id")
                crew_info = fetch_crew(movie_id)
                movies.append(
                    {
                        "Title": item.get("title"),
                        "Original Title": item.get("original_title"),
                        "Genres": ", ".join(genres),
                        "Language": item.get("original_language"),
                        "Release Year": item.get("release_date", "")[:4],
                        "Rating": item.get("vote_average"),
                        "Vote Count": item.get("vote_count"),
                        "Popularity": item.get("popularity"),
                        "Description": item.get("overview"),
                        "Poster Path": (
                            f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}"
                            if item.get("poster_path")
                            else None
                        ),
                        "Adult": item.get("adult", False),
                        "Video": item.get("video", False),
                        "Director": crew_info.get("Director", None),
                    }
                )
        else:
            print(f"Failed to fetch data for page {page}: {response.status_code}")
    return movies


def fetch_series_by_language(total_pages, genre_mapping, language, include_adult=False):
    series = []
    for page in range(1, total_pages + 1):
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "sort_by": "popularity.desc",
            "page": page,
            "include_adult": include_adult,
            "with_original_language": language,  # Filter by language
        }
        response = requests.get(SERIES_URL, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            for item in results:
                genres = [
                    genre_mapping.get(genre_id, "Unknown")
                    for genre_id in item.get("genre_ids", [])
                ]
                series.append(
                    {
                        "Title": item.get("name"),
                        "Original Title": item.get("original_name"),
                        "Genres": ", ".join(genres),
                        "Language": item.get("original_language"),
                        "Release Year": item.get("first_air_date", "")[:4],
                        "Rating": item.get("vote_average"),
                        "Vote Count": item.get("vote_count"),
                        "Popularity": item.get("popularity"),
                        "Description": item.get("overview"),
                        "Poster Path": (
                            f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}"
                            if item.get("poster_path")
                            else None
                        ),
                    }
                )
        else:
            print(f"Failed to fetch data for page {page}: {response.status_code}")
    return series
