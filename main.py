from fastapi import FastAPI, HTTPException
from model.mapper import get_instructors, get_courses, get_instructor_by_id, get_course_by_id, get_all_tags, search_courses, search_courses_by_tag

instructors = get_instructors()
courses = get_courses()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/instructor/{id}")
async def get_instructor(id: int):
    instructor = get_instructor_by_id(id)
    if instructor == None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


@app.get("/course/{id}")
async def get_course(id: int):
    course = get_course_by_id(id)
    if course == None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.get("/tag")
async def get_tags():
    tags =  get_all_tags()
    return {
        "total": len(tags),
        "error": None,
        "data": tags,
    }


@app.get("/search/title/{query}")
async def search_course(query: str):
    found_courses = search_courses(query)
    return {
        "total": len(found_courses),
        "error": None,
        "data": found_courses,
    }


@app.get("/search/tag/{query}")
async def search_course(query: str):
    found_courses = search_courses_by_tag(query)
    return {
        "total": len(found_courses),
        "error": None,
        "data": found_courses,
    }