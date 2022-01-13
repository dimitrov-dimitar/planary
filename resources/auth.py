from flask import request
from flask_restful import Resource
from managers.auth import AuthManager
from managers.user import UserManager
from schemas.request.users import LoginUserSchema, RegisterUserSchema
from util.decorators import validate_schema


class Register(Resource):
    @validate_schema(RegisterUserSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(LoginUserSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200
