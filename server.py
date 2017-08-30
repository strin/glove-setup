from flask import Flask, request, jsonify
from redisdb import redis_store
import json

STORE_NAME='word2vec'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def query():
    data = request.json

    word = data['word']

    vec = json.loads(redis_store.hget(STORE_NAME, word).decode('ascii'))

    return jsonify({
        'vec': list(vec)
    })

if __name__ == '__main__':
    app.run(debug=False, port=5900, host='0.0.0.0')
