import time
import redis
from flask import Flask, jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_page_count():
    retries = 3
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# Home route
@app.route('/')
def home():
    count = get_page_count()
    return jsonify({'message': 'Welcome to the Flask App!', 'visit_count': count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
