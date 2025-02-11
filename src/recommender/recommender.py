import pandas as pd
from recommender.config import BASE_PATH
from sentence_transformers import SentenceTransformer

movies = pd.read_csv(BASE_PATH / "data/processed_data/movies.csv")
series = pd.read_csv(BASE_PATH / "data/processed_data/series.csv")

movies["Tags"] = (
    movies["Description"] + " " + movies["Genres"] + " " + movies["Director"]
)
series["Tags"] = series["Description"] + " " + series["Genres"]

model = SentenceTransformer("all-MiniLM-L6-v2")

movie_embeddings = model.encode(movies["Tags"].tolist())
series_embeddings = model.encode(series["Tags"].tolist())

movie_similarity = model.similarity(movie_embeddings, movie_embeddings)
series_similarity = model.similarity(series_embeddings, series_embeddings)
