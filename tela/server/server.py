from flask import Flask, request, jsonify
import redis
import os
import sys
import traceback

app = Flask(__name__)

# Verbose logging
print("Starting server application...")
print(f"REDIS_HOST: {os.getenv('REDIS_HOST', 'Not Set')}")
print(f"REDIS_PORT: {os.getenv('REDIS_PORT', 'Not Set')}")

try:
    # Connect to Redis using environment variables
    redis_client = redis.Redis(
        host=os.getenv('REDIS_HOST', 'redis'),
        port=int(os.getenv('REDIS_PORT', 6379)),
        db=0,
        decode_responses=True,
        # Add connection timeout and retry configurations
        socket_timeout=5,
        socket_connect_timeout=5,
        retry_on_timeout=True
    )

    # Test Redis connection
    redis_client.ping()
    print("Successfully connected to Redis!")

except Exception as e:
    print("Failed to connect to Redis:")
    print(traceback.format_exc())
    sys.exit(1)

@app.route('/')
def home():
    return "Server is running! Redis Data Storage API"

@app.route('/api/data', methods=['POST'])
def save_data():
    try:
        data = request.json
        key = data.get('key')
        value = data.get('value')
        
        if key and value:
            redis_client.set(key, value)
            return jsonify({"status": "success", "message": f"Data saved with key: {key}"})
        return jsonify({"status": "error", "message": "Invalid data format"}), 400
    except Exception as e:
        print(f"Error saving data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/data/<key>', methods=['GET'])
def get_data(key):
    try:
        value = redis_client.get(key)
        if value:
            return jsonify({"status": "success", "data": value})
        return jsonify({"status": "error", "message": "Key not found"}), 404
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)