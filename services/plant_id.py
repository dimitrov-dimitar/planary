import base64
import requests
# import json
from flask_restful import Resource
from flask import request
from urllib.request import urlopen 
from decouple import config

from managers.services import Service

# url = 'https://littleprinceplants.com/wp-content/uploads/2020/03/Echeveria-subsessilis-Morning-Beauty-Succulent-March4-scaled.jpg'
# url =  'https://plant.id/media/images/757562b36f1942209d4c96720967dfe8.jpg'
# url = 'https://thumbs.dreamstime.com/b/succulent-plant-12848856.jpg'
# url = 'https://t4.ftcdn.net/jpg/03/20/24/31/360_F_320243196_dpDfqhd0wo3jFiZsgW0m4cPMCfX68a9b.jpg'


class PlantIdServices(Resource):
    def post(self):
        url = Service.ulr_identification(request.get_json())

        images = [base64.b64encode(urlopen(url).read()).decode("ascii")]
        json_data = {
            "images": images,
            # "modifiers": ["similar_images"],
            "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
        }
        response = requests.post(
            "https://api.plant.id/v2/identify",
            json=json_data,
            headers={
                "Content-Type": "application/json",
                "Api-Key": f"{config('API_KEY_PLANT')}"
            }).json()
        return response, 200



# print(response)
# for suggestion in response["suggestions"]:
#     print(suggestion["plant_name"])   
#     print(suggestion["plant_details"]["common_names"]) 
#     print(suggestion["plant_details"]["url"])  