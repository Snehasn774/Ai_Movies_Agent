from model.multilingual_recommender import MovieRecommender

rec = MovieRecommender("data/movies.csv")

print("\n=== GENRE SEARCH: Action ===")
print(rec.recommend_by_genre("Action")[["title", "genres"]])

print("\n=== DESCRIPTION SEARCH: dreams ===")
print(rec.recommend_by_keyword("dreams")[["title", "description"]])

print("\n=== SEMANTIC SEARCH: 'movies about love' ===")
print(rec.recommend_similar("movies about love"))

