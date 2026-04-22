# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Pandas, and Scikit-learn. This system suggests movies similar to a given movie based on features like genres, keywords, tagline, cast, and director.

---

## 📌 Features

- Recommends movies based on content similarity
- Uses TF-IDF Vectorization for text processing
- Applies Cosine Similarity to find similar movies
- Handles missing data efficiently
- Supports approximate movie name matching using difflib

---

## 🛠️ Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn

---

## 📂 Project Structure

movie-recommender/

│

├── movies.csv # Dataset file

├── recommender.py # Main Python script

├── README.md # Project documentation


---

## ⚙️ How It Works

1. Load dataset (movies.csv)
2. Select important features:
   - genres
   - keywords
   - tagline
   - cast
   - director
3. Combine features into a single string
4. Convert text data into numerical vectors using TF-IDF
5. Compute similarity using Cosine Similarity
6. Recommend top similar movies

---

## 🚀 Installation

1. Clone the repository:

git clone  https://github.com/SaiAnil07/Movie-Recommendation-System.git

cd movie-recommender

2. Install dependencies:

pip install numpy pandas scikit-learn

---

## ▶️ Usage


recommend_movies("Avatar")

Example Output:
['Avatar: The Way of Water', 'Guardians of the Galaxy', 'Interstellar']

🧠 Function Description
recommend_movies(movie_name, top_n=10)
movie_name: Input movie title
top_n: Number of recommendations (default = 10)

Returns a list of recommended movie titles.

📊 Dataset

Make sure your dataset (movies.csv) contains the following columns:

title
genres
keywords
tagline
cast
director

⚠️ Notes

Ensure movies.csv is in the same directory as the script
Movie names should be close to actual titles for better matching
Uses approximate matching, so small typos are handled

🔮 Future Improvements

Add a web interface (Flask/React)
Use deep learning embeddings (BERT)
Include user-based recommendations
Add movie posters and ratings

👨‍💻 Author

Developed by Sai Anil Uppu
