# fastAPI

Multiverse Project

Schemas

- Automatic ddata validation and conversion
- Persistence using sqlmodel
- Auto-generated documentation
  Authentication with oauth

1. Intro

- FastAPI
  That and why
  Compare with other frameworks
- Project
  Overview
  Requirements

source code: https://github.com/codesensei-courses/fastapi_fundamentals

2. First Steps

- Create a Fast API app
  Explore
  Run
- Check result in browser
  REST Api
  Auto-generated documentation
- Common Problems
- FastAPI code execution
  Async

install fastapi run the command : python3 -m pip install "fastapi[all]" - extra dependenies are installed using [all]
run the application/loading the server: uvicorn carsharing:app --reload
uvicorn is the HTTP server
carsharing is the name of the file containing the application object
app is the name of the application object inside that file

when you open the browser you see the welcome message. if you add '/docs' to the browser you can see the requests your application runs

you can add '/redoc' to see another documentation

creating a database model class - we need to install sql; python3 -m pip install sqlmodel

authentication: python3 -m pip install "passlib[bcrypt]"

pytest: python3 -m pip install pytest

3. Create a Fast API app
   Explore
   Run

- Check result in browser
  REST Api
  Auto-generated documentation
- Common Problems
- FastAPI code execution
  Async

- Read - only opeartions
  Serve car data
  Filter cars
- Parameters
  Query parameters
  Path parameters
- Type hints
  Validation, conversion and more
- Return 404 Not Found
- Debugging

4. Serving Structured Data Using Pydantic Models

- Operations that add/change data
  -Structured data
  Pydantic model classes
  Save/load as JSON file
- Input and Output schemas
  Request and Response body
- Calling our API using Postman
  Using openapi.json
  https://pydantic-docs.helpmanual.io/

5. Using a Database with FastAPI

- SQL on SQLAlchemy + Pydantic
- Create data model classes
- Create a DB connection n
- Crud operations
- Relations
- Transactions
  Session

SQLModel

- Based on SQLAlchemy
  Popular ORM library
  Mature, robust
  Supports many databases
- Also based on Pydantic
  Model classes are Pydantic Models
  Allows easy intgration with FastAPI
  Same creator(Sebastian Ramirez)
- SQLModel
  New, still being developed
  Gives access to the power of SQLAlchemy
  https://sqlodel.tiangolo.com

6. HTTP and Fast API

- Custom response types
- Serving a website
  Dynamic HTML with Jinja
  Processing Form Data
- Status codes and error handling
- Headers and cookies
- Middleware
- Organising our code with APIRouter

7. Authentication

- Adding a User Class
  DB Options:unique, index
  Password hashing
- HTTP Basic Auth
  Nested dependencies
  -OAuth 2
