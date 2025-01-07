from fastapi import FastAPI, HTTPException, Query
from model.mapper import *

instructors = get_instructors()
courses = get_courses()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/instructors/{id}")
async def get_instructor(id: int):
    instructor = get_instructor_by_id(id)
    if instructor == None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


@app.get("/courses")
async def get_course(ids: List[int] = Query(...)):
    all_courses = get_courses()
    
    courses = []
    for id in ids:
        courses.append(get_course_by_id(id))

    return {
        "total": len(courses),
        "error": None,
        "data": courses,
    }


@app.get("/tag")
async def get_tags():
    tags =  get_all_tags()
    return {
        "total": len(tags),
        "error": None,
        "data": tags,
    }

@app.get("/tags/{category}")
async def get_course_by_category(category: str):
    courses = get_course_by_tag(category)
    return {
        "total": len(courses),
        "error": None,
        "data": courses,
    }


@app.get("/search/popular")
async def search_popular_courses():
    courses = get_popular_courses(10)
    return {
        "total": len(courses),
        "error": None,
        "data": courses,
    }


@app.get("/search/courses/{query}")
async def search_course(query: str):
    found_courses = search_courses(query)
    return {
        "total": len(found_courses),
        "error": None,
        "data": found_courses,
    }


@app.get("/search/tags/{query}")
async def search_course(query: str):
    found_courses = search_courses_by_tag(query)
    return {
        "total": len(found_courses),
        "error": None,
        "data": found_courses,
    }