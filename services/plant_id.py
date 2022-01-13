import base64
from urllib.request import urlopen

import requests
from decouple import config
from flask import request
from flask_restful import Resource
from managers.services import Service


class PlantIdServices(Resource):
    def post(self):
        url = Service.ulr_identification(request.get_json())

        images = [base64.b64encode(urlopen(url).read()).decode("ascii")]
        json_data = {
            "images": images,
            # "modifiers": ["similar_images"],
            "plant_details": ["common_names", "url", "wiki_description", "taxonomy"],
        }
        response = requests.post(
            "https://api.plant.id/v2/identify",
            json=json_data,
            headers={
                "Content-Type": "application/json",
                "Api-Key": f"{config('API_KEY_PLANT')}",
            },
        ).json()
        return response, 200
