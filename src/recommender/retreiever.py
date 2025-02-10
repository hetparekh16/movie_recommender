import requests
from dotenv import load_dotenv
from recommender.config import BASE_URL
import os
import asyncio
import aiohttp

load_dotenv() 

async def fetch_movies(total_pages):
    movies = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, page) for page in range(1, total_pages + 1)]
        results = await asyncio.gather(*tasks)  # Fetch all pages in parallel
        movies.extend([movie for page in results for movie in page])  # Flatten results
    return movies
