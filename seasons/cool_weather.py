# import season class to inherit
from .season import Season


# create a cool weather class
class CoolWeather(Season):
    def __init__(self, season_name):
        super().__init__(season_name)
        self.weather_type = "cool"
