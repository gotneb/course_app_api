from dataclasses import dataclass
from .lesson import Lesson


@dataclass
class Course:
    id: int
    instructor_id: int
    title: str
    thumbnail_url: str
    rating: float
    price: float
    enrolled: int
    description: str
    tags: list[str]
    lessons: list[Lesson]