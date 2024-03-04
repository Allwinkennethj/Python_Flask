from marshmallow import fields, Schema

class AdminSchema(Schema):
    username = fields.String()
    name = fields.String()
