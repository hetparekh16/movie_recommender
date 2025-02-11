from recommender.config import BASE_PATH
import pandas as pd

bollywood_movies = pd.read_csv(BASE_PATH / "data/raw_data/bollywood_movies.csv")
hollywood_movies = pd.read_csv(BASE_PATH / "data/raw_data/hollywood_movies.csv")
bollywood_series = pd.read_csv(BASE_PATH / "data/raw_data/bollywood_series.csv")
hollywood_series = pd.read_csv(BASE_PATH / "data/raw_data/hollywood_series.csv")
