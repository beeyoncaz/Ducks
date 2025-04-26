import uvicorn #brings in uvicorn library which allows python web apps to run
import logging #allows you to log messages, helpful for debugging
logger = logging.getLogger('uvicorn.error')

from fastapi import FastAPI # imports the FastAPI class to create the web API
from typing import List  # allows you to use List 
from app.duck import Duck  # imports the Duck model 
from pydantic import BaseModel, Field # used to define data validation models (like Duck)


app = FastAPI() # creates an instance of the FastAPI application
ducks = [] # creates an in-memory list to store duck objects (a fake "database")


@app.post("/ducks/") # defines a POST endpoint at /ducks/
async def duck_data(duck: Duck):  # receives JSON matching the Duck model and stores it
    ducks.append(duck)  # appends the received duck to the in-memory list
    logger.info("added duck to duck database") # logs the event for debugging
    return "done!" # returns confirmation string

@app.get("/ducks/") # defines a GET endpoint at /ducks/
async def get_ducks(): # returns all ducks stored in memory
    return ducks


@app.put("/ducks/{duck_id}") # creates PUT endpoint of URL /ducks/{duck_id}
def update_duck(id: int, duck: Duck): # defines functions update_duck with parameters id and duck
   ducks[id-1] = duck # updates duck list at position id-1 with new duck info
   return ducks # returns duck list
 
@app.delete("/ducks/{duck_id}") # creates DELETE endpoint of URL /ducks/{duck_id}
def delete_duck(id: int): # defines delete_duck dunction with parameter id
   ducks.pop(id-1) # removes item from ducks list at index id-1
   return ducks # returns duck list


# @app.put("/ducks/{duck_name}") 
# async def update_duck(duck_name: str, updated_duck: Duck):
#     for index, duck in enumerate(ducks):
#         if duck.name == duck_name:
#             ducks[index] = updated_duck
#             logger.info(f"Updated duck: {duck_name}")
#             return {"message": "Duck updated!"}
#     return {"error": "Duck not found"}, 404

# @app.delete("/ducks/{duck_name}")
# async def delete_duck(duck_name: str):
#     for index, duck in enumerate(ducks):
#         if duck.name == duck_name:
#             deleted_duck = ducks.pop(index)
#             logger.info(f"Deleted duck: {duck_name}")
#             return {"message": "Duck deleted!"}
#     return {"error": "Duck not found"}, 404

#look through code, write tests (run on port 8000, tests use python request library)put endpoint (update duck - change name), delete endpoint (delete a duck)