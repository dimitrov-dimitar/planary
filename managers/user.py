from db import db
from models.users import PlantModel, UserModel
from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                raise InternalServerError(
                    "Server is unavailable. Please try again later"
                )
        return user

    @staticmethod
    def login(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user
