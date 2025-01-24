from flask import Flask,render_template, request
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    cities = [
        "Toronto",
        "Montreal",
        "Calgary",
        "Ottawa",
        "Edmonton",
        "Vancouver",
        "Winnipeg",
        "Halifax",
        "Quebec City",
        "Victoria",
        "Hamilton",
        "Saskatoon",
        "Kitchener",
        "London",
        "St. John's",
        "Mississauga",
        "Regina"
    ]
    return render_template('weather.html', cities=cities)

@app.route('/result', methods=['POST'])
def result():
    city = request.form.get('city')
    weather_data = query_api(city)
    if not weather_data:
        return render_template('result.html', error="Could not fetch data.")
    return render_template('result.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
