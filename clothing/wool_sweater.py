# importing clothing class for inheritance on wool sweater class and cold weather for composition
from seasons.cold_weather import ColdWeather
from .clothing import Clothing


# creating wool sweater class
class WoolSweater(Clothing):
    def __init__(self, name, color, size, description):
        super().__init__(name, color, size, description)
        self.season = ColdWeather("Winter")
