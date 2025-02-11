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


def recommend_movies(movie_title):
    # First pass: Description-based similarity
    movie_index = movies[movies["Title"] == movie_title].index[0]
    movie_similarity_scores = list(enumerate(movie_similarity[movie_index]))
    top_movies = sorted(
        movie_similarity_scores, key=lambda x: x[1].item(), reverse=True
    )

    # Return only movie titles
    return [movies.iloc[i[0]]["Title"] for i in top_movies[1:11]]


def recommend_series(series_title):
    # First pass: Description-based similarity
    series_index = series[series["Title"] == series_title].index[0]
    description_similarity = list(enumerate(series_similarity[series_index]))
    top_series = sorted(description_similarity, key=lambda x: x[1].item(), reverse=True)

    # Return only series titles
    return [series.iloc[i[0]]["Title"] for i in top_series[1:11]]
