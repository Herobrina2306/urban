from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_dict() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=2, max_length=15, description="Enter name", example='Sasha')],
        age: Annotated[int, Path(ge=16, le=120, description='Enter age', example='25')]) -> dict:
    new_user = User(id=len(users)+1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(description="Enter id", example='5')],
                      username: Annotated[
                          str, Path(min_length=2, max_length=15, description="Enter name", example='Sasha')],
                      age: Annotated[int, Path(ge=16, le=120, description='Enter age', example='25')]) -> str:
    try:
        user = users[user_id - 1]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(description="Enter id", example='5')]) -> str:
    try:
        us = users.pop(user_id+1)
        return us
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
