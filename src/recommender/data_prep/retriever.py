import requests
from dotenv import load_dotenv
from recommender.config import BASE_URL, BASE_PATH
import os
import asyncio
import aiohttp
import chromadb

load_dotenv()
chroma_client = chromadb.PersistentClient(path=f"{BASE_PATH}/data")
collection = chroma_client.get_or_create_collection(name="movies")


async def fetch_genre(language):
    async with aiohttp.ClientSession() as session:
        params = {"api_key": os.getenv("API_KEY"), "language": language}
        async with session.get(
            f"{BASE_URL}/genre/movie/list", params=params
        ) as response:
            data = await response.json()
            return {genre["id"]: genre["name"] for genre in data.get("genres", [])}


async def fetch_page(session, page, language):
    params = {
        "api_key": os.getenv("API_KEY"),
        "page": page,
        "language": language,
    }
    async with session.get(f"{BASE_URL}/discover/movie", params=params) as response:
        return (
            (await response.json()).get("results", []) if response.status == 200 else []
        )


async def fetch_movies(total_pages, language):
    # movies = []
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_page(session, page, language) for page in range(1, total_pages + 1)
        ]
        results = await asyncio.gather(*tasks)
        movies = [movie for page in results for movie in page]
    return movies


async def store_movies(total_pages, language):
    movies = await fetch_movies(total_pages, language)
    genre_mapping = await fetch_genre(language)
    for movie in movies:
        collection.add(
            ids=str(movie["id"]),
            documents=[
                movie["overview"] if movie["overview"] else "No description available"
            ],
            metadatas=[
                {
                    "adult": movie["adult"],
                    "genres": ", ".join(
                        [
                            genre_mapping.get(genre_id, "Unknown")
                            for genre_id in movie.get("genre_ids", [])
                        ]
                    ),
                    "original_language": movie["original_language"],
                    "original_title": movie["original_title"],
                    "overview": movie["overview"],
                    "popularity": movie["popularity"],
                    "poster_path": (
                        f"https://image.tmdb.org/t/p/w500{('poster_path')}"
                        if movie.get("poster_path")
                        else ""
                    ),
                    "release_date": movie["release_date"],
                    "title": movie["title"],
                    "vote_average": movie["vote_average"],
                    "vote_count": movie["vote_count"],
                }
            ],
        )


asyncio.run(store_movies(500, "en"))
