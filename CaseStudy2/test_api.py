import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

# ---------------- FIXTURE ----------------
@pytest.fixture
def new_movie():
    return {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 200
    }

# ---------------- PARAMETERIZED TEST ----------------
@pytest.mark.parametrize("movie_id", [101])
def test_get_movie_by_id(movie_id):
    response = requests.get(f"{BASE_URL}/api/movies/{movie_id}")
    assert response.status_code == 200
    assert response.json()["id"] == movie_id


def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_movie(new_movie):
    response = requests.post(f"{BASE_URL}/api/movies", json=new_movie)
    assert response.status_code == 201
    assert response.json()["message"] == "Movie added successfully"


def test_update_movie():
    payload = {
        "movie_name": "Interstellar Updated",
        "price": 300
    }
    response = requests.put(f"{BASE_URL}/api/movies/101", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Movie updated"


def test_delete_movie():
    response = requests.delete(f"{BASE_URL}/api/movies/102")
    assert response.status_code == 200
    assert response.json()["message"] == "Movie deleted"


def test_book_ticket():
    payload = {
        "movie_id": 101,
        "tickets": 2
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert response.status_code == 201
    assert response.json()["total_price"] == 2 * 300


def test_booking_failure():
    payload = {
        "movie_id": 999,
        "tickets": 2
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert response.status_code == 404
    assert "error" in response.json()
