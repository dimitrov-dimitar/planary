from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.plants import PlantManager
from models.users import PlantModel
from schemas.request.plants import PlantCreateRequestSchema
from util.decorators import validate_schema


class CreatePlant(Resource):
    def get(self):
        pass

    @auth.login_required
    @validate_schema(PlantCreateRequestSchema)
    def post(self):
        user_id = auth.current_user()
        plant = PlantManager.create(request.get_json(), user_id.id)
        return plant
