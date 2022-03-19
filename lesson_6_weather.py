from pprint import pprint
import requests
from keys import APIkey
from datetime import datetime
from app import db
from app.models import WeatherTable, WeatherTableHistory

"""links to weather API and libray with icons:
https://openweathermap.org/forecast5
https://openweathermap.org/api/one-call-api
https://libraries.io/npm/weathericons
https://rapidapi.com/wettercom-wettercom-default/api/forecast9/"""


def take_city_name():
    city_list = []
    """take city name from list of city names"""
    with open("city_names.txt") as file:
        for row in file:
            city_list.append(row.strip())
    return city_list


def take_coordinates_of_city(city):
    """take geographic coordinates to find a city name"""
    # city = take_city_name()
    limit = 1
    coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={APIkey}"
    coordinates_city_link = coordinates_city
    city = city
    coordinats_to_cityname = requests.get(coordinates_city_link)
    lat = coordinats_to_cityname.json()[0].get("lat")
    lon = coordinats_to_cityname.json()[0].get("lon")

    return lat, lon, city


