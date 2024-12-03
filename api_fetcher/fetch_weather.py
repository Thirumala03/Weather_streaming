import requests
from mqtt_publisher.publish_to_mqtt import publish_weather

def fetch_weather(city):
    api_key = "6af2d08cf3d44b6381381736242611"
    base_url = "http://api.weatherapi.com/v1/current.json?"
    url = f"{base_url}key={api_key}&q=sivakasi"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        publish_weather(weather_data)
    else:
        print("Failed to fetch weather data")
