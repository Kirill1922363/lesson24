import logging
from flask import Flask, jsonify

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route('/error', methods=['GET'])
def error():
    app.logger.error("Simulated error occurred on /error endpoint")
    return jsonify({"error": "Something went wrong"}), 500

if __name__ == '__main__':
    app.run(debug=True)
