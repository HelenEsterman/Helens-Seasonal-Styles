# importing season class to inherit properties
from .season import Season


# create a cold weather class
class ColdWeather(Season):
    def __init__(self, season_name):
        super().__init__(season_name)
        self.weather_type = "cold"
