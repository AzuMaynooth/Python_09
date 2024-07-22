import datetime
import requests
import json
import os
from geopy.geocoders import Nominatim

class WeatherForecast:
    def __init__(self, file_path):
        self.file_path = file_path
        self.forecasts = self.read_results()

    def read_results(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save_results(self):
        with open(self.file_path, "w") as file:
            json.dump(self.forecasts, file)

    def __setitem__(self, date, weather):
        self.forecasts[date] = weather
        self.save_results()

    def __getitem__(self, date):
        return self.forecasts.get(date, None)

    def __iter__(self):
        return iter(self.forecasts)

    def items(self):
        return ((date, weather) for date, weather in self.forecasts.items())

# Helper functions
def get_next_day():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def get_weather_status(latitude, longitude, date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=auto&start_date={date}&end_date={date}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        if weather_data.get("daily") and weather_data["daily"].get("precipitation_sum"):
            precipitation = weather_data["daily"]["precipitation_sum"][0]
            return precipitation
    return None

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Main script
results_file = "weather_results.json"
weather_forecast = WeatherForecast(results_file)

while True:
    city_name = input("Enter the city name: \n"
                      "If you want to end the program write end: ")
    if city_name.lower() == 'end':
        break

    latitude, longitude = get_coordinates(city_name)
    if latitude is None or longitude is None:
        print(f"Could not find coordinates for {city_name}. Please try again.\n")
        continue

    while True:
        time_str = input("Add date (YYYY-MM-DD) \n or\n press enter to get tomorrow's information: ")
        if not time_str:
            time_str = get_next_day()
            break
        try:
            datetime.datetime.strptime(time_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Incorrect date format, please try it again.")

    if time_str in weather_forecast:
        precipitation = weather_forecast[time_str]
    else:
        precipitation = get_weather_status(latitude, longitude, time_str)
        weather_forecast[time_str] = precipitation

    if precipitation is None:
        print(f"No data available for {city_name} on {time_str}\n")
    elif precipitation > 0.0:
        print(f"Rainfall for {city_name} on {time_str}: {precipitation} mm.")
    else:
        print(f"No rain for {city_name} on {time_str}\n")

# Example of how to use the weather_forecast object
for date, weather in weather_forecast.items():
    print(f"Date: {date}, Weather: {weather}")