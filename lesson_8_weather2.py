import requests
from keys import APIkey
from datetime import datetime, timedelta
from pprint import pprint
import os

"""links to weather API and libray:
https://openweathermap.org/api/one-call-api"""

# x = sys.argv
x = [APIkey, "2022-03-30"]
APIkey = x[0]


def check_input():
    if len(x) > 1:
        date = datetime.strptime(x[1], "%Y-%m-%d").strftime('%Y-%m-%d')
        input_dict = {"day": date}
    elif len(x) == 1:
        tomorrow = datetime.now().date() + timedelta(days=1)
        input_dict = {"day": f'{tomorrow}'}
    else:
        print("Input data are incorrect")

    return input_dict


def take_coordinates_of_city():
    """take city name to find geographic coordinates"""
    city = "Warsaw"
    limit = 1
    coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?" \
                       f"q={city}&limit={limit}&appid={APIkey}"
    coordinates_city_link = coordinates_city
    city_name_coordinates = requests.get(coordinates_city_link)
    lat = city_name_coordinates.json()[0].get("lat")
    lon = city_name_coordinates.json()[0].get("lon")
    return lat, lon


def take_forecast_for_city():
    """take geographic coordinates to find a city and take parameters
    from the link and return JSON file"""
    coordinates = take_coordinates_of_city()
    lat = coordinates[0]
    lon = coordinates[1]
    units = "metric"
    part = "current,minutely,hourly,alerts"

    weather_download_link = f"https://api.openweathermap.org/data" \
                            f"/2.5/onecall?lat={lat}&lon={lon}" \
                            f"&units={units}&exclude={part}&appid={APIkey}"
    weather_data = requests.get(weather_download_link).json()
    return weather_data


def create_dict_with_weather():
    """create dictionary with weather conditions:
    date and level of raining - for 8 day forecast"""

    weather_data = take_forecast_for_city()
    weather_day_dict_hist = {}
    weather_day_dict = {}
    for idx in range(8):
        weather_date = datetime.fromtimestamp\
            (weather_data["daily"][idx]["dt"]).strftime('%Y-%m-%d')
        weather_rain = weather_data["daily"][idx].get("rain", "no rain")
        weather_day_dict[weather_date] = weather_rain
    weather_day_dict_hist.update(weather_day_dict)
    return weather_day_dict_hist


class WeatherForecast:
    def __init__(self, Apikey):
        self.Apikey = Apikey
        self.take_data = create_dict_with_weather()

    def __setitem__(self, weather_date, weather_rain):
        self.take_data[weather_date] = weather_rain

    def __getitem__(self, weather_date):
        return self.take_data[weather_date]

    def items(self):
        for date, weather in self.take_data.items():
            # print(f"{date}: {weather}")
            yield date, weather

    def __iter__(self):
        for data in self.take_data:
            yield data


wf = WeatherForecast(x[0])

# wf[date]
print(wf["2022-03-30"])

# wf.items()
wf.items()

# wf iterator
for date in wf:
    print(date)







