from marshmallow import Schema, fields, ValidationError

def validate_year(year):
    if year < 0 or year > 2025:
        raise ValidationError("Year must be between 0 and 2025")

class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)
    year = fields.Integer(required=True, validate=validate_year)
