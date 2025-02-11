from recommender.config import BASE_PATH
import pandas as pd

bollywood_movies = pd.read_csv(BASE_PATH / "data/raw_data/bollywood_movies.csv")
hollywood_movies = pd.read_csv(BASE_PATH / "data/raw_data/hollywood_movies.csv")
bollywood_series = pd.read_csv(BASE_PATH / "data/raw_data/bollywood_series.csv")
hollywood_series = pd.read_csv(BASE_PATH / "data/raw_data/hollywood_series.csv")

bollywood_movies.drop(columns=["Writer", "Producer"], inplace=True)
hollywood_movies.drop(columns=["Writer", "Producer"], inplace=True)

bollywood_movies.dropna(inplace=True)
hollywood_movies.dropna(inplace=True)
bollywood_series.dropna(inplace=True)
hollywood_series.dropna(inplace=True)

bollywood_movies.drop_duplicates(inplace=True)
hollywood_movies.drop_duplicates(inplace=True)
bollywood_series.drop_duplicates(inplace=True)
hollywood_series.drop_duplicates(inplace=True)
