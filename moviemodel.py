from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from recommender import recommend_movies  # using your recommender.py logic

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend (HTML/JS) to connect

# API endpoint for recommendations
@app.route("/recommend", methods=["GET"])
def recommend():
    movie = request.args.get("movie")
    if not movie:
        return jsonify({"error": "No movie provided"}), 400
    
    recommendations = recommend_movies(movie)
    return jsonify({"recommendations": recommendations})

# (Optional) Serve your index.html if placed in templates/
@app.route("/")
def home():
    return render_template("index.html")  # needs templates/index.html

if __name__ == "__main__":
    app.run(debug=True)
