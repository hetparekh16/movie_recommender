import requests
from dotenv import load_dotenv
from recommender.config import BASE_URL, BASE_PATH
import os
import asyncio
import aiohttp
import chromadb
