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
