from db import db
from models.users import PlantModel


class PlantManager:
    @staticmethod
    def create(plant_data, user_id):
        plant_data["user_id"] = user_id
        plant = PlantModel(**plant_data)
        db.session.add(plant)
        db.session.commit()
        return plant
