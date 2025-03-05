from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
        }
