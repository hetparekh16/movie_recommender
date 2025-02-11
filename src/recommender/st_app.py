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


def display_movie_cards(movies):
    for i in range(0, len(movies), 4):  # Display 4 cards per row
        cols = st.columns(4)  # Create 4 columns
        for col, movie in zip(cols, movies[i : i + 4]):
            with col:
                st.markdown(
                    f"""
                    <div style="border: 1.5px solid #ccc; border-radius: 10px; padding: 10px; margin: 10px; text-align: center; background-color: #f9f9f9;">
                        <img src="{movie['Poster Path']}" alt="{movie['Title']}" style="width: 100%; height: 450px; object-fit: cover; border-radius: 10px;" />
                        <div style="height: 60px;  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                            <h4 style="margin-top: 10px; font-size: 24px; color: black;">{movie['Title']}</h4>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


nav_option = st.radio(
    "Navigation",
    ("Movies", "Series", "Watch something similar"),
    horizontal=True,
)
