import requests
from decouple import config
from flask import request
from flask_restful import Resource
from managers.services import Service


class WeatherForecast(Resource):
    def post(self):
        lat, lon = Service.location(request.get_json())

        response = requests.post(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={config('API_KEY_WEATHER')}",
        ).json()
        return response, 200
