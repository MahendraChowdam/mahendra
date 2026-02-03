from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    movies.append(data)
    return jsonify({"message": "Movie added successfully"}), 201

@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify({"message": "Movie updated"}), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.get_json()
    movie_id = data.get("movie_id")
    tickets = data.get("tickets")

    for movie in movies:
        if movie["id"] == movie_id:
            booking = {
                "movie_id": movie_id,
                "tickets": tickets,
                "total_price": tickets * movie["price"]
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Movie not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
