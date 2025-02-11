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
