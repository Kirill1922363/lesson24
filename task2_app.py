import logging
from flask import Flask, request, jsonify

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def user():
    data = request.get_json()

    if "username" not in data:
        app.logger.warning("Request to /user is missing 'username' field")
        return jsonify({"error": "Username is required"}), 400

    app.logger.info(f"User request received for username: {data['username']}")
    return jsonify({"message": f"Hello, {data['username']}!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
