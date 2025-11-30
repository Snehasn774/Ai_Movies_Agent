import streamlit as st
import pandas as pd

# ---------------------------
# Load movies.csv
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

df = load_data()

# ---------------------------
# UI Title
# ---------------------------
st.title("🎬 Movie Search System")

st.write("Search movies by Actor, Year, Genre, Language, or Title")

# ---------------------------
# User Inputs
# ---------------------------
actor = st.text_input("🔍 Search by Actor name")
genre = st.text_input("🎭 Search by Genre (Action, Drama, Romance...)")
year = st.text_input("📅 Search by Year")
language = st.text_input("🌐 Search by Language (Kannada, Telugu...)")
title = st.text_input("🔎 Search by Movie Title")

if st.button("Search Movies"):
    result = df.copy()

    # ---------------------------
    # Filters (UPDATED)
    # ---------------------------

    # Actor filter → partial match, case-insensitive
    if actor:
        result = result[result["actor"].str.contains(actor, case=False, na=False)]

    # Genre filter
    if genre:
        result = result[result["genre"].str.contains(genre, case=False, na=False)]

    # Language filter
    if language:
        result = result[result["language"].str.contains(language, case=False, na=False)]

    # Movie title filter
    if title:
        result = result[result["title"].str.contains(title, case=False, na=False)]

    # Year filter
    if year:
        result = result[result["year"] == int(year)]

    # ---------------------------
    # Show results
    # ---------------------------
    st.success(f"Found {len(result)} movies 🎉")

    st.dataframe(result)
