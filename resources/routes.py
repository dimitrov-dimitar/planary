from resources.auth import Register, Login
from services.plant_id import PlantIdServices
from services.weather import WeatherForecast

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (PlantIdServices, "/identification"),
    (WeatherForecast, "/weather"),
)
