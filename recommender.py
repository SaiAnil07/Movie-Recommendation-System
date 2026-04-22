import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

# Load dataset
movies_data = pd.read_csv('movies.csv')

# Preprocess
selected_features = ['genres','keywords','tagline','cast','director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('') 

# Combine features into one string per movie
combined_features = (
    movies_data['genres'] + " " +
    movies_data['keywords'] + " " +
    movies_data['tagline'] + " " +
    movies_data['cast'] + " " +
    movies_data['director']
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Similarity matrix
similarity = cosine_similarity(feature_vectors)

list_of_all_titles = movies_data['title'].tolist()

def recommend_movies(movie_name, top_n=10):
    # Find the closest matching movie title
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    if not find_close_match:
        return ["No match found! Try another movie."]
    
    close_match = find_close_match[0]
    
    # Use pandas index directly instead of 'index' column
    index_of_the_movie = movies_data[movies_data.title == close_match].index[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended = []
    for i, movie in enumerate(sorted_similar_movies[1:top_n+1], start=1):
        index = movie[0]
        title_from_index = movies_data.iloc[index]['title']
        recommended.append(title_from_index)
    
    return recommended
