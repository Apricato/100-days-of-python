import requests
from datetime import datetime

# Parameters for the sunrise-sunset API
parameters = {
    "lat": 21.88234,
    "lng": -102.28259,
    "formatted": 0
}

# Get sunrise and sunset times
response_api = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_api.raise_for_status()
sun_data = response_api.json()

sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

# Get the current position of the ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

longitude = iss_data["iss_position"]["longitude"]
latitude = iss_data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(f"ISS Position: {iss_position}")