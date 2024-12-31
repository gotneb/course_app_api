from .instructor import Instructor
from .lesson import Lesson
from .course import Course
from typing import List

import json


def get_instructors() -> List[Instructor]:
    with open("data/instructors.json", "r") as file:
        data = json.load(file)

    print("Loaded")
    instructors = [Instructor(**instructor) for instructor in data]
    return instructors


def get_courses() -> List[Course]:
    with open("data/courses.json", "r") as file:
        data = json.load(file)
    
    courses = []
    for course_data in data:
        lessons = [Lesson(**lesson) for lesson in course_data["lessons"]]
        
        course = Course(
            lessons=lessons,
            **{key: value for key, value in course_data.items() if key != "lessons"}
        )
        courses.append(course)
    
    return courses