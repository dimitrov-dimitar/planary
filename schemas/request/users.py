from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))
