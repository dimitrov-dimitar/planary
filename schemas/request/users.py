from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class LoginUserSchema(BaseUserSchema):
    pass


class RegisterUserSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
