from flask import Flask, render_template, jsonify
from database.mongodb_handler import get_latest_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/live-weather')
def live_weather_api():
    data = get_latest_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
