import requests

API_KEY = '03e894209c41440e33e3d6a0bf760774'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

ICON_MAP = {
    "01d": "wi-day-sunny.svg",     # Clear sky (day)
    "01n": "wi-night-clear.svg",   # Clear sky (night)
    "02d": "wi-day-cloudy.svg",    # Few clouds (day)
    "02n": "wi-night-alt-cloudy.svg", # Few clouds (night)
    "03d": "wi-cloud.svg",         # Scattered clouds
    "03n": "wi-cloud.svg",
    "04d": "wi-cloudy.svg",        # Broken clouds
    "04n": "wi-cloudy.svg",
    "09d": "wi-showers.svg",       # Shower rain
    "09n": "wi-showers.svg",
    "10d": "wi-day-rain.svg",      # Rain (day)
    "10n": "wi-night-rain.svg",    # Rain (night)
    "11d": "wi-thunderstorm.svg",  # Thunderstorm
    "11n": "wi-thunderstorm.svg",
    "13d": "wi-snow.svg",          # Snow
    "13n": "wi-snow.svg",
    "50d": "wi-fog.svg",           # Mist
    "50n": "wi-fog.svg"
}

def query_api(city):
    try:
        response = requests.get(BASE_URL.format(city, API_KEY))
        data = response.json()
        if "weather" in data and len(data["weather"]) > 0:
            icon_code = data["weather"][0]["icon"]
            # Replace the icon code with the mapped filename
            data["weather"][0]["icon"] = ICON_MAP.get(icon_code, "default-icon.svg")
        return data
    except Exception as e:
        print(e)
        return None
