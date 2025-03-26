from datetime import datetime

from pydantic import BaseModel, field_validator, constr
from typing_extensions import Optional


class BookSchema(BaseModel):
    title: constr(min_length=2, max_length=100)
    author: constr(min_length=2, max_length=50)
    year: int
    id: Optional[int] = None

    @field_validator("title")
    def validate_title(cls, title: str):
        if not any(c.isalpha() for c in title):
            raise ValueError("Title must contain at least one letter")
        return title

    @field_validator("year")
    def validate_year(cls, year: int):
        current_year = datetime.now().year
        if not 1 <= year <= current_year:
            raise ValueError(
                f"Year must be between 1 and {current_year}"
            )
        return year
