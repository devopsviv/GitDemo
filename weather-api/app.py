from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Weather API",
        "status": "running"
    })

@app.route('/weather')
def weather():
    return jsonify({
        "location": "INDIA",
        "temperature": 12,
        "condition": "Partly Cloudy",
        "humidity": 65
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
