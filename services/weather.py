from flask_restful import Resource
from managers.services import Service
from decouple import config
from flask import request
import requests


class WeatherForecast(Resource):
    def post(self):
        lat, lon = Service.location(request.get_json())

        response = requests.post(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={config('API_KEY_WEATHER')}",
).json()
        return response, 200
