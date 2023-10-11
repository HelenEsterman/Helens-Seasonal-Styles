# import season class for hot weather class to inherit
from .season import Season


# create hot weather class
class HotWeather(Season):
    def __init__(self, season_name):
        super().__init__(season_name)
        self.weather_type = "hot"
