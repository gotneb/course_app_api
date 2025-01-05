from dataclasses import dataclass
from .lesson import Lesson
from .instructor import Instructor
from typing import Optional


@dataclass
class Course:
    id: int
    instructor_id: int
    instructor: Optional[Instructor]
    title: str
    thumbnail_url: str
    rating: float
    price: float
    enrolled: int
    description: str
    tags: list[str]
    lessons: list[Lesson]