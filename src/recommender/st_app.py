import streamlit as st
from recommender.recommender import recommend_movies, recommend_series
from recommender.config import BASE_PATH
import pandas as pd

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data():
    movies = BASE_PATH / "data/processed_data/movies.csv"
    series = BASE_PATH / "data/processed_data/series.csv"
    return (
        pd.read_csv(movies),
        pd.read_csv(series),
    )


movies = load_data()[0]
series = load_data()[1]
