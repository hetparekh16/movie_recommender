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
