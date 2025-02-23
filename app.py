from flask import Flask, request, jsonify
from geopy.distance import geodesic

app = Flask(__name__)

# Sample driver locations (Latitude, Longitude)
drivers = [
    {"id": 1, "name": "Driver A", "location": (40.730610, -73.935242)},
    {"id": 2, "name": "Driver B", "location": (40.712776, -74.005974)},
    {"id": 3, "name": "Driver C", "location": (40.758896, -73.985130)}
]

@app.route('/')
def home():
    return "Welcome to AI Autonomous Ride Backend!"

@app.route('/request_ride', methods=['POST'])
def request_ride():
    data = request.get_json()
    user_location = data.get('location')  # Expected format: (lat, lon)

    if not user_location:
        return jsonify({"error": "Location is required"}), 400

    nearest_driver = find_nearest_driver(user_location)
    return jsonify({"message": "Ride requested!", "driver": nearest_driver})

def find_nearest_driver(user_location):
    """Find the nearest driver to the user's location."""
    nearest_driver = min(drivers, key=lambda d: geodesic(user_location, d['location']).km)
    return nearest_driver

@app.route('/complete_ride', methods=['POST'])
def complete_ride():
    return jsonify({"message": "Ride completed successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
