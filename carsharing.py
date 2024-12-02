#first we create an object and store it in the app variable

import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from db import engine
from routers import cars, web, auth
from routers.cars import BadTripException

app = FastAPI(title="Car Sharing")
app.include_router(web.router)
app.include_router(cars.router)
app.include_router(auth.router)

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 #create a global application object and call the constructor. the object represents our application

#create the database on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.exception_handler(BadTripException)
async def unicorn_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad Trip"},
    )


# @app.middleware("http")
# async def add_cars_cookie(request: Request, call_next):
#     response = await call_next(request)
#     response.set_cookie(key="cars_cookie", value="you_visited_the_carsharing_app")
#     return response


#add an operation called get_cars()
#served at /api/cars
#returns all car data
#    @app.get("/api/cars")
#    def get_cars():
#        return db


#FastAPI will call get_session and store result in session parameter
#
if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)



#Sum
#query parameters = arguments to our function/opeartion/endpoint
#this passed into to the url
#its better to add type hints: itgnored by python, used by Fast API for conversion, validation and documentation
#optinal query parameters by searching for doors and size by using None = None using the union operator which means 'or' - size is a str or none
#when we are searching by id we use the path prameters in a curly braces. this cannot be optiional 
#we used an exception to return 

#Sum for using pydantic Models
#Inherit from pydantic.BaseModel
#List fields with types as class AttributesImplCan include (collections of) other Model objects
#more info: https://pydantic-docs.helpmanual.io/
#Pydantic Models in request and response
#id is a path parameter(from URL)
#new_data is a pydantic model so its read from the request body
#return type for function is not used by fastapi
#to set schema for response, use response_model in the decorator
