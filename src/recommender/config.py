from pathlib import Path

BASE_PATH = Path(__file__).parent.parent.parent
BASE_URL = "https://api.themoviedb.org/3"
MOVIE_URL = f"{BASE_URL}/discover/movie"
GENRE_URL = f"{BASE_URL}/genre/movie/list"
SERIES_URL = f"{BASE_URL}/discover/tv"
