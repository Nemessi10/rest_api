from datetime import datetime
from marshmallow import Schema, fields, ValidationError, validates

def validate_year(year):
    current_year = datetime.now().year
    if year < 1 or year > current_year:
        raise ValidationError(f"Year must be between 1 and {current_year}")

def validate_non_empty_string(value):
    if not value.strip():
        raise ValidationError("Field cannot be empty or contain only spaces")

class BookSchema(Schema):
    title = fields.String(required=True, validate=validate_non_empty_string,
                          error_messages={"required": "Title is required"})
    author = fields.String(required=True, validate=validate_non_empty_string,
                           error_messages={"required": "Author is required"})
    year = fields.Integer(required=True, validate=validate_year,
                          error_messages={"required": "Year is required"})

    @validates("title")
    def validate_title(self, value):
        if len(value) < 2 or len(value) > 100:
            raise ValidationError("Title must be between 2 and 100 characters")
        if not value.strip():
            raise ValidationError("Title must contain at least one character")

    @validates("author")
    def validate_author(self, value):
        if len(value) < 2 or len(value) > 50:
            raise ValidationError("Author's name must be between 2 and 50 characters")
