from marshmallow import Schema, fields, validate


class PlantCreateRequestSchema(Schema):
    latin_name = fields.String(required=True, validate=validate.Length(max=120))
    catalogue_name = fields.String(required=True, validate=validate.Length(max=120))
    description = fields.String(required=True, validate=validate.Length(max=1024))
