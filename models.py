from dataclasses import dataclass


@dataclass
class Book:
    author: str
    book_format: str
    description: str
    genre: str
    isbn: str
    link: str
    pages: int
    rating: int
    reviews: str
    title: str
    total_ratings: str
