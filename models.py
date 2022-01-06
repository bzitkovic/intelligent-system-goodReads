from dataclasses import dataclass


@dataclass
class Book:
    author: str
    book_format: str
    description: str
    genres: list[str]
    isbn: str
    link: str
    pages: int
    rating: float
    reviews: int
    title: str
    total_ratings: int
