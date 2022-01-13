from flask import request
from flask_restful import Resource
from managers.auth import AuthManager
from managers.user import UserManager



class Register(Resource):
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200
