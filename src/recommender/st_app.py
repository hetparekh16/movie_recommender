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

if nav_option == "Movies":
    st.title("Welcome to the Movie Recommender System!")
    st.write("Use the filters on the sidebar to refine your search.")

    # Sidebar Filters
    st.sidebar.header("Filter Movies")

    # Filter by Release Year
    min_year, max_year = st.sidebar.slider(
        "Release Year",
        min_value=int(movies["Release Year"].min()),
        max_value=int(movies["Release Year"].max()),
        value=(2000, 2025),
    )

    # Filter by Adult Content
    include_adult = st.sidebar.checkbox("Include Adult Content", value=False)

    # Apply Filters
    filtered_df = movies[
        (movies["Release Year"] >= min_year)
        & (movies["Release Year"] <= max_year)
        & (movies["Adult"] == include_adult if not include_adult else True)
    ]

    # Display Filtered Results
    st.subheader("Movies")

    # Show 20 random movies initially or filtered movies
    if filtered_df.empty:
        st.write("No movies match your filters.")
    else:
        movies_to_display = (
            filtered_df.sample(20) if len(filtered_df) > 20 else filtered_df
        )
        display_movie_cards(movies_to_display.to_dict(orient="records"))


elif nav_option == "Series":
    st.title("Welcome to the Series Recommender System!")
    st.write("Use the filters on the sidebar to refine your search.")

    # Sidebar Filters
    st.sidebar.header("Filter Series")

    # Filter by Release Year
    min_year, max_year = st.sidebar.slider(
        "Release Year",
        min_value=int(series["Release Year"].min()),
        max_value=int(series["Release Year"].max()),
        value=(2000, 2025),
    )

    # Apply Filters
    filtered_df = series[
        (series["Release Year"] >= min_year) & (series["Release Year"] <= max_year)
    ]

    # Display Filtered Results
    st.subheader("Movies")

    # Show 20 random movies initially or filtered movies
    if filtered_df.empty:
        st.write("No movies match your filters.")
    else:
        series_to_display = (
            filtered_df.sample(20) if len(filtered_df) > 20 else filtered_df
        )
        display_movie_cards(series_to_display.to_dict(orient="records"))


# Watch something similar
elif nav_option == "Watch something similar":
    st.title("Watch Something Similar")
    st.write("Enter the title of a movie or series to find similar content.")

    st.sidebar.header("Choose a Movie or Series")

    option = st.sidebar.radio(
        "Choose movie or series", ["Movie :movie_camera:", "Series :tv:"]
    )

    if option == "Movie :movie_camera:":
        movie_title = st.selectbox("Enter a movie title", movies["Title"])
        if st.button("Recommend Movies"):
            recommended_movies = recommend_movies(movie_title)
            display_movie_cards(
                movies[movies["Title"].isin(recommended_movies)].to_dict(
                    orient="records"
                )
            )

    else:
        series_title = st.selectbox("Enter a series title", series["Title"])
        if st.button("Recommend Series"):
            recommended_series = recommend_series(series_title)
            display_movie_cards(
                series[series["Title"].isin(recommended_series)].to_dict(
                    orient="records"
                )
            )
