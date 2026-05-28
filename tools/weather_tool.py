import requests


def get_weather(city):
    coordinates = {
        "goa": (15.2993, 74.1240),
        "bangalore": (12.9716, 77.5946),
        "delhi": (28.7041, 77.1025),
        "mumbai": (19.0760, 72.8777),
        "hyderabad": (17.3850, 78.4867),
        "chennai": (13.0827, 80.2707),
        "kolkata": (22.5726, 88.3639),
        "jaipur": (26.9124, 75.7873)
    }

    city = city.lower()

    if city not in coordinates:
        return "Weather data not available"

    lat, lon = coordinates[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    try:
        response = requests.get(url)
        if response.status_code !=200:
            return "could not fetuch weather data"
        
    
        data = response.json()

        weather = data.get("current_weather", {})

        temperature = weather.get("temperature")
        windspeed = weather.get("windspeed")

        return (
        f"Current temperature in {city.title()}: {temperature}°C\n"
        f"Wind Speed: {windspeed} km/h"
      ) 
    except Exception as e :
        return f"Weather API Error: {e}"

