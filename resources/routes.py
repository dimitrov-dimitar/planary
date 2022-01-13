from services.plant_id import PlantIdServices
from services.weather import WeatherForecast

from resources.auth import Login, Register
from resources.plants import CreatePlant

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (CreatePlant, "/plants/create"),
    (PlantIdServices, "/identification"),
    (WeatherForecast, "/weather"),
)
