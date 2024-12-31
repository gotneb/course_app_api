from fastapi import FastAPI
from model.mapper import get_instructors, get_courses


# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
instructors = get_instructors()
for i in instructors:
    print(f'Instructor: {i.name}')


courses = get_courses()
for c in courses:
    print(f'Title: {c.title}')