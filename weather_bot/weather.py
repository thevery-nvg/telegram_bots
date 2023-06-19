from os import getenv

from dotenv import load_dotenv
import requests

from typing import Literal
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum

load_dotenv()


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temperature: float
    temperature_feeling: float
    description: str
    wind_speed: float
    wind_direction: str
    sunrise: datetime
    sunset: datetime

    def output(self):
        return f'Сейчас на улице:\n' \
               f'Температура: {self.temperature}ºC\n' \
               f'Чувствуется как {self.temperature_feeling}ºC\n' \
               f'Ветер {self.wind_direction} со скоростью {self.wind_speed} м/c\n' \
               f'Восход: {self.sunrise}\n' \
               f'Закат : {self.sunset}'


def _parse_openweather_response(openweather_dict: dict) -> Weather:
    return Weather(
        location=openweather_dict['name'],
        temperature=openweather_dict['main']['temp'],
        temperature_feeling=openweather_dict['main']['feels_like'],
        description=str(openweather_dict['weather'][0]['description']).capitalize(),
        sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
        sunset=_parse_sun_time(openweather_dict, 'sunset'),
        wind_speed=openweather_dict['wind']['speed'],
        wind_direction=_parse_wind_direction(openweather_dict)
    )


def _parse_sun_time(openweather_dict: dict, time: Literal["sunrise", "sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict['sys'][time])


def _parse_wind_direction(openweather_dict: dict) -> str:
    degrees = openweather_dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0
    return WindDirection(degrees).name


def get_weather(lat: float, lon: float) -> Weather:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={getenv('WEATHER')}&units=metric"
    weather = requests.get(url).json()
    return _parse_openweather_response(weather)


