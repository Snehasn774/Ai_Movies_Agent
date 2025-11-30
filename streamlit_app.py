import streamlit as st
import pandas as pd
import requests

# ------------------------------------------------------
# TMDB API KEY
# ------------------------------------------------------
TMDB_API_KEY = "YOUR_REAL_TMDB_API_KEY"


# ------------------------------------------------------
# ROBUST POSTER FETCH FUNCTION (MULTIPLE FALLBACKS)
# ------------------------------------------------------
def get_poster_url(title):
    """Fetch movie poster with fallback title variations."""
    
    # Clean common issues
    title_clean = title.replace(":", "").replace("-", " ").strip()

    # Variations to try
    search_variants = [
        title,
        title_clean,
        title.split("(")[0].strip(),
        title.split(":")[0].strip(),
        title.split("-")[0].strip(),
    ]

    for query in search_variants:
        try:
            url = "https://api.themoviedb.org/3/search/movie"
            params = {"api_key": TMDB_API_KEY, "query": query}
            response = requests.get(url, params=params).json()

            if "results" in response and len(response["results"]) > 0:
                poster_path = response["results"][0].get("poster_path")
                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500{poster_path}"
        except:
            pass

    # Fallback placeholder
    return "https://via.placeholder.com/150x225?text=No+Poster"


# ------------------------------------------------------
# LOAD MOVIES CSV
# ------------------------------------------------------
movies = pd.read_csv("movies.csv")

movies["actors"] = movies["actors"].astype(str).str.lower()
movies["genre"] = movies["genre"].astype(str).str.lower()
movies["title"] = movies["title"].astype(str)

movies["year"] = pd.to_numeric(movies["year"], errors="coerce")
movies["rating"] = pd.to_numeric(movies["rating"], errors="coerce")

# ------------------------------------------------------
# STREAMLIT UI
# ------------------------------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown("""
<h1 style='color:#4A47FF;'>🎬 Movie Recommender With Posters</h1>
<p>Search by <b>Actor</b>, <b>Genre</b>, or <b>Year</b>.</p>
""", unsafe_allow_html=True)

choice = st.selectbox(
    "Choose search type:",
    ["Recommend by Actor", "Recommend by Genre", "Recommend by Year"]
)


# Input Field
if choice == "Recommend by Actor":
    user_input = st.text_input("Enter actor name:").lower().strip()

elif choice == "Recommend by Genre":
    user_input = st.text_input("Enter genre:").lower().strip()

else:
    user_input = st.number_input("Enter year:", min_value=1900, max_value=2025, step=1)
    user_input = int(user_input)


# ------------------------------------------------------
# FILTERING LOGIC
# ------------------------------------------------------
results = pd.DataFrame()

if user_input:

    # ACTOR
    if choice == "Recommend by Actor":
        results = movies[movies["actors"].str.contains(user_input)]

    # GENRE
    elif choice == "Recommend by Genre":
        results = movies[movies["genre"].str.contains(user_input)]

    # YEAR
    else:
        results = movies[movies["year"] == user_input]

    # Only movies up to 2025
    results = results[results["year"] <= 2025]

    # Most recent first
    results = results.sort_values(by="year", ascending=False)

    # Only latest 5
    results = results.head(5)

    # Reset index
    results = results.reset_index(drop=True)


# ------------------------------------------------------
# SHOW RESULTS
# ------------------------------------------------------
if not user_input:
    st.stop()

if results.empty:
    st.warning("No movies found!")
else:

    icon = "🎭" if choice == "Recommend by Actor" else "🎞️" if choice == "Recommend by Genre" else "📅"
    st.markdown(f"<h3>{icon} Results:</h3>", unsafe_allow_html=True)

    for _, row in results.iterrows():

        poster = get_poster_url(row["title"])

        st.markdown(f"""
            <div style='display:flex; gap:20px; padding:15px; 
                        background:#f3f3f3; border-radius:12px; 
                        margin-bottom:15px; box-shadow:0 2px 6px rgba(0,0,0,0.15);'>

                <img src="{poster}" 
                     style="width:140px; height:auto; border-radius:10px;" />

                <div>
                    <h3 style="margin:0;">{row['title']}</h3>
                    <p>📅 <b>Year:</b> {int(row['year'])}</p>
                    <p>⭐ <b>Rating:</b> {row['rating']}/5</p>
                </div>

            </div>
        """, unsafe_allow_html=True)
