import pandas as pd
from recommender.config import BASE_PATH
from sentence_transformers import SentenceTransformer

movies = pd.read_csv(BASE_PATH / "data/processed_data/movies.csv")
series = pd.read_csv(BASE_PATH / "data/processed_data/series.csv")
