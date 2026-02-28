import streamlit as st
import pandas as pd
import joblib
import requests
import random

# ========== PAGE CONFIG ==========
st.set_page_config(layout="wide", page_title="Bollywood AI Recommender")

# ========== LIGHT ELEGANT STYLE ==========
st.markdown("""
<style>
.stApp {
    background-color: #f8f9fa;
    color: #222;
}

h1 {
    font-size: 42px;
    font-weight: 700;
    color: #111;
}

h2 {
    margin-top: 40px;
}

section[data-testid="stSidebar"] {
    background-color: #ffffff;
}

.stButton>button {
    background-color: #e63946;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 8px 18px;
}

.stButton>button:hover {
    background-color: #d62828;
}
</style>
""", unsafe_allow_html=True)

# ========== LOAD MODEL ==========
data = joblib.load("model/bollywood_model.pkl")
df = data["data"]
similarity_matrix = data["similarity"]

title_column = df.columns[0]

# ========== TMDB ==========
TMDB_API_KEY = "6cd9c3a50f11cc3c8d9b5b5225ee129b"

def fetch_poster(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": title}
    response = requests.get(url, params=params).json()

    if response.get("results"):
        poster_path = response["results"][0].get("poster_path")
        backdrop = response["results"][0].get("backdrop_path")

        if backdrop:
            backdrop_url = f"https://image.tmdb.org/t/p/w1280{backdrop}"
        else:
            backdrop_url = None

        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            poster_url = None

        return poster_url, backdrop_url

    return None, None

# ========== HERO SECTION ==========
st.markdown("## 🎬 Bollywood AI Movie Recommender")
st.markdown("Discover movies by genre and similarity using AI.")

st.divider()

# ========== GENRE FILTER ==========
if "Genre" in df.columns:
    # Extract unique genres (split if multiple genres separated by comma)
    all_genres = df["Genre"].dropna().str.split(",").explode().str.strip()
    unique_genres = sorted(all_genres.unique())
else:
    unique_genres = []

selected_genre = st.selectbox("🎭 Select Genre", unique_genres)

# Filter movies by selected genre
genre_filtered = df[df["Genre"].str.contains(selected_genre, case=False)]

# ========== TRENDING IN GENRE ==========
st.subheader(f"🔥 Trending in {selected_genre}")

if "Rating" in df.columns:
    trending = genre_filtered.sort_values(by="Rating", ascending=False).head(5)
else:
    trending = genre_filtered.head(5)

cols = st.columns(5)

for i in range(min(5, len(trending))):
    with cols[i]:
        movie_title = trending.iloc[i][title_column]
        poster, _ = fetch_poster(movie_title)
        if poster:
            st.image(poster, use_container_width=True)
        st.caption(movie_title)

st.divider()

# ========== SELECT MOVIE ==========
selected_movie = st.selectbox(
    "🎥 Select a Movie",
    genre_filtered[title_column].values
)

top_n = st.slider("Number of Recommendations", 1, 10, 5)

# ========== RECOMMEND ==========
if st.button("Recommend"):

    index = df[df[title_column] == selected_movie].index[0]
    scores = list(enumerate(similarity_matrix[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    st.subheader("✨ You May Also Like")

    cols = st.columns(top_n)

    for idx, (i, score) in enumerate(scores):
        with cols[idx]:
            movie = df.iloc[i]
            movie_title = movie[title_column]
            poster, _ = fetch_poster(movie_title)

            if poster:
                st.image(poster, use_container_width=True)

            st.caption(movie_title)
            st.write(f"{round(score*100,1)}% Match")

st.divider()

st.markdown(
    "<center style='opacity:0.6;'>Built with ❤️ by Boomi Rao | AI/ML Project</center>",
    unsafe_allow_html=True
)