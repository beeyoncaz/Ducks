from pydantic import BaseModel

class Duck(BaseModel):
    breed: str
    age: int