from .instructor import Instructor
from .lesson import Lesson
from .course import Course
from typing import List
import random

import json


def get_instructors() -> List[Instructor]:
    with open("data/instructors.json", "r") as file:
        data = json.load(file)

    print("Loaded")
    instructors = [Instructor(**instructor) for instructor in data]
    return instructors


def get_courses_with_instructors() -> List[Course]:
    courses = get_courses()

    for course in courses:
        if hasattr(course, "instructor_id"):
            course.instructor = get_instructor_by_id(course.instructor_id)

    return courses


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

        course.instructor = get_instructor_by_id(course.instructor_id)

        courses.append(course)
    
    return courses


def get_instructor_by_id(id: int) -> Instructor:
    instructors = get_instructors()

    for i in instructors:
        if i.id == id:
            return i
    return None


def get_popular_courses(n: int) -> List[Course]:
    courses = get_courses()
    n = min(n, len(courses))

    return random.sample(courses, n)


def get_course_by_tag(tag: str) -> List[Course]:
    n = min(5, len(courses))

    if tag.lower() == "all":
        return random.sample(courses, n)

    courses = get_courses()
    courses_with_tags = []

    for c in courses:
        if tag in c.tags:
            courses_with_tags.append(c)
    
    return courses_with_tags


def get_course_by_id(id: int) -> Course:
    courses = get_courses()

    for c in courses:
        if c.id == id:
            c.instructor = get_instructor_by_id(c.instructor_id)
            return c
    return None


def get_all_tags() -> List[str]:
    return ["coding", "language", "design", "science", "marketing", "business"]


def search_courses(search_query: str) -> List[Course]:
    courses = get_courses()
    return [
        course for course in courses
        if search_query.lower() in course.title.lower() or any(search_query.lower() in tag.lower() for tag in course.tags)
    ]


def search_courses_by_tag(tag: str) -> List[Course]:
    courses = get_courses()
    n = min(5, len(courses))

    if tag.lower() == "all":
        return random.sample(courses, n)
    

    return [
        course for course in courses
        if any(tag.lower() == t.lower() for t in course.tags)
    ]