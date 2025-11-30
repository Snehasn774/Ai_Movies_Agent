import streamlit as st
from model.multilingual_recommender import MultilingualMovieRecommender

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# Load model
recommender = MultilingualMovieRecommender("data/movies.csv")

# Page Title
st.markdown("""
<h1 style='color:#4A4AFF; font-size:40px;'>
🎬 Multilingual Movie Recommender
</h1>
""", unsafe_allow_html=True)

st.write("Find movies by **Actor**, **Genre**, or **Year**.")


# --- Dropdown ---
choice = st.selectbox(
    "Choose what you want:",
    ["Recommend by Actor", "Recommend by Genre", "Recommend by Year"]
)


# --- Input Fields ---
query = st.text_input(
    f"Enter {choice.split()[-1].lower()}:",
    placeholder="Type here..."
)


# When user enters something
if query:

    # Get results
    if choice == "Recommend by Actor":
        results = recommender.recommend_by_actor(query)

        st.markdown("### 🎭 Movies with this actor:")

    elif choice == "Recommend by Genre":
        results = recommender.recommend_by_genre(query)

        st.markdown("### 🎬 Movies in this genre:")

    elif choice == "Recommend by Year":
        results = recommender.recommend_by_year(query)

        st.markdown("### 📅 Movies from this year:")


    # Handle no results
    if isinstance(results, str):
        st.warning(results)
    else:
        # Display each movie in a card UI
        for _, row in results.iterrows():

            title = row["title"]
            year = row["year"]
            rating = row["rating"]

            # Movie Card
            st.markdown(f"""
                <div style="
                    padding:15px;
                    margin:10px 0;
                    border-radius:12px;
                    background:#f3f3f3;
                    box-shadow:0 2px 6px rgba(0,0,0,0.1);
                ">
                    <h4 style="margin:0; font-size:22px;">🎞️ {title}</h4>
                    <p style="margin:5px 0;">📅 <strong>Year:</strong> {year}</p>
                    <p style="margin:5px 0;">⭐ <strong>Rating:</strong> {rating}/5</p>
                </div>
            """, unsafe_allow_html=True)
