import pytest
from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get("username") == "admin" and data.get("password") == "secret":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401



@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_login_success(client):
    response = client.post(
        '/login',
        json={"username": "admin", "password": "secret"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Login successful"


def test_login_invalid_credentials(client):
    response = client.post(
        '/login',
        json={"username": "user", "password": "wrong"}
    )

    assert response.status_code == 401
    data = response.get_json()
    assert data["message"] == "Invalid credentials"


def test_login_missing_fields(client):
    response = client.post(
        '/login',
        json={}
    )

    assert response.status_code == 401


if __name__ == '__main__':
    app.run(debug=True)
