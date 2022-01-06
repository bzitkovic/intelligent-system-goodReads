from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    author: str
    book_format: str
    description: str
    genres: List[str]
    isbn: str
    link: str
    pages: int
    rating: float
    reviews: int
    title: str
    total_ratings: int
