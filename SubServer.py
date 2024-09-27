from flask import Flask, jsonify, request
import random

from keep_alive import keep_alive
keep_alive()

app = Flask(__name__)

@app.route('/v1/games/<int:place_id>/servers/Public', methods=['GET'])
def get_servers(place_id):
    # Simulate server data
    servers = [
        {"id": random.randint(1, 1000), "status": "available", "playerCount": random.randint(0, 50)}
        for _ in range(5)  # Simulate 5 servers
    ]

    # Handle pagination with cursor (for demonstration, simply return empty response)
    cursor = request.args.get('cursor')
    if cursor:
        return jsonify({"data": [], "nextPageCursor": None})  # Simulate no further pages
    
    return jsonify({"data": servers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all interfaces, port 5000
